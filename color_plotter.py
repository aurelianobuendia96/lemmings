import os, io
import matplotlib.pyplot as plt
from google.cloud import vision

def ColorPlot(path):
    # Instantiates a client
    os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = r'gold-atlas.json'
    client = vision.ImageAnnotatorClient()

    # The name of the image file to annotate
    file_name = os.path.abspath(path)

    # Loads the image into memory
    with io.open(file_name, 'rb') as image_file:
        content = image_file.read()
    image = vision.Image(content=content)

    # Performs label detection on the image file
    response = client.image_properties(image=image)
    props = response.image_properties_annotation

    
    rgb_list = []
    score_list = []
    color_list = props.dominant_colors.colors

    for color in props.dominant_colors.colors:
        rgb_list = rgb_list + [(int(color.color.red), int(color.color.green), int(color.color.blue))]
        score_list = score_list + [color.score]

    
    percentages = [f"{value*100:.2f}%" for value in score_list]

    # Convert RGB values to hex strings for plotting
    colors = ['#%02x%02x%02x' % rgb for rgb in rgb_list]

    # Create bar chart
    plt.bar(colors, percentages, color=colors, width=1.2)

    # Add labels and title
    plt.xlabel('RGB values')
    plt.xticks(rotation=45)
    plt.ylabel('Percentage')
    plt.title('Bar chart of RGB values and percentages')

    # Show plot
    plt.show()





