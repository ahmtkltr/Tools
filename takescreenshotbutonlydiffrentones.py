Python 3.12.2 (tags/v3.12.2:6abddd9, Feb  6 2024, 21:26:36) [MSC v.1937 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import time
... import os
... from PIL import Image, ImageChops
... import pyautogui
... 
... def take_screenshot():
...     timestamp = int(time.time())
...     screenshot_path = f"screenshot_{timestamp}.png"
...     pyautogui.screenshot(screenshot_path)
...     return screenshot_path
... 
... def compare_images(img1, img2, threshold):
...     image1 = Image.open(img1)
...     image2 = Image.open(img2)
... 
...     if image1.size != image2.size or image1.mode != image2.mode:
...         return False
... 
...     diff = ImageChops.difference(image1, image2)
...     diff = diff.convert('L')
...     total_diff = sum(diff.getdata()) / (image1.size[0] * image1.size[1])
... 
...     return total_diff <= threshold
... 
... def delete_duplicates(screenshot_list, threshold=5):
...     i = 0
...     while i < len(screenshot_list):
...         j = i + 1
...         while j < len(screenshot_list):
...             if compare_images(screenshot_list[i], screenshot_list[j], threshold):
...                 os.remove(screenshot_list[j])
...                 del screenshot_list[j]
...             else:
...                 j += 1
...         i += 1
... 
def main():
    screenshot_list = []
    try:
        while True:
            screenshot_path = take_screenshot()
            screenshot_list.append(screenshot_path)
            delete_duplicates(screenshot_list)
            time.sleep(10)  # 10 saniye bekleme
    except KeyboardInterrupt:
        print("Program kullanıcı tarafından sonlandırıldı.")

if __name__ == "__main__":
