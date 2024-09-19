import os
import random
import shutil

def split_data(source_dir, train_dir, test_dir, valid_dir, split_ratio=(0.7, 0.15, 0.15)):
    # Get all the image filenames
    images = os.listdir(source_dir)
    random.shuffle(images)
    
    train_size = int(split_ratio[0] * len(images))
    test_size = int(split_ratio[1] * len(images))
    
    train_images = images[:train_size]
    test_images = images[train_size:train_size + test_size]
    valid_images = images[train_size + test_size:]
    
    def copy_images(image_list, target_dir):
        if not os.path.exists(target_dir):
            os.makedirs(target_dir)
        for img in image_list:
            shutil.copy(os.path.join(source_dir, img), os.path.join(target_dir, img))
    
    copy_images(train_images, train_dir)
    copy_images(test_images, test_dir)
    copy_images(valid_images, valid_dir)

# Example usage
split_data('C:/Users/Vishwak/Smart Vision/Smart-Vision/ai/data/dataset/pills/', 
           'C:/Users/Vishwak/Smart Vision/Smart-Vision/ai/data/dataset/medication/train/', 
           'C:/Users/Vishwak/Smart Vision/Smart-Vision/ai/data/dataset/medication/test/', 
           'C:/Users/Vishwak/Smart Vision/Smart-Vision/ai/data/dataset/medication/valid/')