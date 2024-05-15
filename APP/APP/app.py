from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def resolution_changer():
    if request.method == 'POST':
        width = int(request.form['width'])
        height = int(request.form['height'])
        percentage = int(request.form['percentage'])

        if request.form['operation'] == 'subtract':
            percentage = 100 - percentage
        else:
            percentage += 100

        new_width = int(width * percentage / 100)
        new_height = int(height * percentage / 100)

        original_pixels = width * height
        new_pixels = new_width * new_height

        example_width = 1920
        example_height = 1080
        example_new_width = int(example_width * percentage / 100)
        example_new_height = int(example_height * percentage / 100)
        example_original_pixels = example_width * example_height
        example_new_pixels = example_new_width * example_new_height

        return render_template('result.html', width=width, height=height, percentage=percentage,
                               new_width=new_width, new_height=new_height,
                               original_pixels=original_pixels, new_pixels=new_pixels,
                               example_width=example_width, example_height=example_height,
                               example_new_width=example_new_width, example_new_height=example_new_height,
                               example_original_pixels=example_original_pixels, example_new_pixels=example_new_pixels)

    return render_template('index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)