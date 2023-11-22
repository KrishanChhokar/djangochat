# from django.shortcuts import render
# from .utils import generate_image

# def generate_image_home(request):
#     if request.method == 'POST':
#         prompt = request.POST.get('prompt', '')  # Get the prompt from the form
#         generated_image_path = generate_image(prompt)
#         return render(request, 'generate_image_home.html', {'generated_image_path': generated_image_path})
#     else:
#         return render(request, 'generate_image_home.html', {'generated_image_path': None})

from django.shortcuts import render
from .utils import generate_image
from PIL import Image
import io

def generate_image_home(request):
    if request.method == 'POST':
        prompt = request.POST.get('prompt', '')  # Get the prompt from the form
        generated_image_path = generate_image(prompt)

        try:
            with open(generated_image_path, "rb") as image_file:
                image_data = image_file.read()
                image = Image.open(io.BytesIO(image_data))
                # Rest of your image processing code

            return render(request, 'generate_image_home.html', {'generated_image_path': generated_image_path})
        except Exception as e:
            print(f"Error opening image: {str(e)}")
            # Handle the error, e.g., return a default image or message
    else:
        return render(request, 'generate_image_home.html', {'generated_image_path': None})
