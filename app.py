# ==============================================#
#                  module                      #
# ==============================================#
import cv2
import os


# ==============================================#
#               print a image                  #
# ==============================================#
# img = cv2.imread('img/screenshot.jpg')
# height, width = img.shape[:2]  # stored by (height,width,dimension)

# print('img width:', width)
# print('img height:', height)

# cv2.imshow('img', img)
# cv2.waitKey(0)

# ===============================================#
#                print a video                   #
# ===============================================#

# cap = cv2.VideoCapture('mov/cartest.mp4')

# # video information
# width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
# height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
# count = cap.get(cv2.CAP_PROP_FRAME_COUNT)//10
# fps = cap.get(cv2.CAP_PROP_FPS)

# print('width:', str(width))
# print('height:', str(height))
# print('count: ', str(count))
# print('FPS', str(fps))


# while (cap.isOpened()):
#     ret, frame = cap.read()
#     if ret:
#         # frame은 이미지 정보이므로 imshow로 읽어 들일수 있음
#         cv2.imshow('frame', frame)
#     if cv2.waitKey(1) & 0XFF == ord('q'):  # press key 'q' to close
#         break

# cap.release()
# cv2.destroyAllWindows()

# ===============================================#
#             make images using video           #
# ===============================================#

# video_path = 'mov/cartest.mp4'
# output_dir = 'snapshot/'
# time_interval = 50  # time interver to save image (it determines count of images)

# # open video file
# cap = cv2.VideoCapture(video_path)
# num = 0
# time_elapsed = 0

# while cap.isOpened():
#     ret, frame = cap.read()
#     if ret:
#         cv2.imshow('frame', frame)

#         if time_elapsed >= time_interval:
#             path = os.path.join(output_dir, f'snapshot_{num}.jpg')
#             cv2.imwrite(path, frame)
#             num += 1
#             time_elapsed = 0  # init time

#         time_elapsed += 1

#         if cv2.waitKey(1) & 0xFF == ord('q'):
#             break
#     else:
#         break

# cap.release()
# cv2.destroyAllWindows()

# ===============================================#
#             make video using images            #
# ===============================================#

# set directory having images
# image_dir = 'snapshot/'

# # set video information
# fps = 30  # frame
# output_video_path = 'new_video/output_video.avi'  # dir path to save video

# # get images file list
# image_files = sorted([os.path.join(image_dir, f) for f in os.listdir(
#     image_dir) if f.startswith('snapshot_') and f.endswith('.jpg')])

# # video setting by first image
# first_image = cv2.imread(image_files[0])
# height, width, layers = first_image.shape

# # VideoWriter 객체 생성
# fourcc = cv2.VideoWriter_fourcc(*'XVID')  # setting codec (using XVID here)
# out = cv2.VideoWriter(output_video_path, fourcc, fps, (width, height))

# # convert img into video
# for image_file in image_files:
#     img = cv2.imread(image_file)
#     out.write(img)

# out.release()
# cv2.destroyAllWindows()

# print("finish making video.")
