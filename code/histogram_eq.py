import cv2
import argparse
import numpy as pb
import glob


def hist_equalization(img):
    """ Normal Histogram Equalization

    Args:
        img : image input with single channel

    Returns:
        : Equalized Image
    """
    array = pb.asarray(img)
    bin_cont = pb.bincount(array.flatten(), minlength=256)
    pixels = pb.sum(bin_cont)
    bin_cont = bin_cont / pixels
    cumulative_sumhist = pb.cumsum(bin_cont)
    map = pb.floor(255 * cumulative_sumhist).astype(pb.uint8)
    arr_list = list(array.flatten())
    eq_arr = [map[p] for p in arr_list]
    arr_back = pb.reshape(pb.asarray(eq_arr), array.shape)
    return arr_back


def ahe(img, rx=136, ry=185):
    """ Adaptive Histogram Equalization

    Args:
        img : image input with single channel
        rx (int, optional): to divide horizontal regions, Note: Should be divisible by image size in x . Defaults to 136.
        ry (int, optional): to divide vertical regions, Note: Should be divisible by image size in y. Defaults to 185.

    Returns:
        : Equalized Image
    """
    v = img
    img_eq = pb.empty((v.shape[0], v.shape[1]), dtype=pb.uint8)
    for i in range(0, v.shape[1], rx):
        for j in range(0, v.shape[0], ry):
            t = v[j:j + ry, i:i + rx]
            c = hist_equalization(t)
            img_eq[j:j + ry, i:i + rx] = c
    return img_eq


def main():
    '''Main Function'''
    # Arguments
    parse = argparse.ArgumentParser()
    parse.add_argument(
        '--FilePath', default='../data_files/adaptive_hist_data',
        help='Images path')
    parse.add_argument(
        "--visualize",
        default=True,
        choices=('True', 'False'),
        help="Shows visualization. Default: False.")
    parse.add_argument(
        "--record",
        default=False,
        choices=('True', 'False'),
        help="Records video (histE.mp4 & AHE.mp4). Default: False.")

    Args = parse.parse_args()
    # Change the file format below if images are in different formats
    file_path = Args.FilePath + '/*.png'
    visualize = str(Args.visualize)
    video_write = str(Args.record)
    fps = 10
    if video_write == str(True):
        fourcc = cv2.VideoWriter_fourcc(*'mp4v')
        out1 = cv2.VideoWriter(
            "..result/histE.mp4", fourcc, fps, (1224, 370))
        out2 = cv2.VideoWriter(
            "..result/AHE.mp4", fourcc, fps, (1224, 370))
        print("Writing to Video...")

    images = sorted(glob.glob(file_path))
    for image in images:
        img = cv2.imread(image, 1)
        # Covert to HSV
        hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
        h, s, v = cv2.split((hsv))
        hist_v = hist_equalization(v)
        # Merge back the channel
        merged_hist = cv2.merge((h, s, hist_v))
        hist = cv2.cvtColor(merged_hist, cv2.COLOR_HSV2BGR)

        ahe_v = ahe(v)
        merged_ahe = cv2.merge((h, s, ahe_v))
        ahe_img = cv2.cvtColor(merged_ahe, cv2.COLOR_HSV2BGR)

        if video_write == str(True):
            out1.write(hist)
            out2.write(ahe_img)
        if visualize == str(True):
            cv2.imshow("Original", img)
            cv2.imshow("Histogram Equalization", hist)
            cv2.imshow("AHE", ahe_img)
            cv2.waitKey(1)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    if video_write == str(True):
        out1.release()
        out2.release()


if __name__ == '__main__':
    main()
