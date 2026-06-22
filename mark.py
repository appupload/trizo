from PIL import Image, ImageDraw

def mark_image(img_path, box_percentages, output_path):
    try:
        with Image.open(img_path) as img:
            draw = ImageDraw.Draw(img)
            width, height = img.size
            
            x1 = int((box_percentages[0] / 100) * width)
            y1 = int((box_percentages[1] / 100) * height)
            x2 = int((box_percentages[2] / 100) * width)
            y2 = int((box_percentages[3] / 100) * height)
            
            line_width = max(3, int(width * 0.015)) 
            draw.rectangle([x1, y1, x2, y2], outline="red", width=line_width)
            
            img.save(output_path)
            print(f"Successfully marked {output_path}")
    except Exception as e:
        print(f"Error marking {img_path}: {e}")

mark_image('img/1.jpg', (10, 75, 90, 85), 'img/1_marked.jpg')
mark_image('img/2.jpg', (35, 62, 65, 68), 'img/2_marked.jpg')
mark_image('img/3.jpg', (20, 68, 80, 72), 'img/3_marked.jpg')
mark_image('img/4.jpg', (5, 48, 95, 58), 'img/4_marked.jpg')
mark_image('img/5.jpg', (80, 3, 95, 10), 'img/5_marked.jpg')
