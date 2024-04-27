from flask import Flask, request, render_template

app = Flask(__name__,
            template_folder='../templates',
            static_folder='../static')


@app.route('/')
def index():
    return '<h1>Hello, World!</h1>'


# @app.errorhandler(404)
# def page_not_found(error):
#     app.logger.warning(error)
#     context = {
#         'title': 'Page not found',
#         'url': request.base_url,
#     }
#     return render_template('404.html', **context), 404


@app.errorhandler(404)
def page_not_found(error):
    """
    Handle 404 errors by logging the error, creating the context, and rendering the 404.html template.

    Args:
        error: The error that occurred.

    Returns:
        The rendered 404.html template with the specified context and status code 404.
    """
    app.logger.warning(error)

    # Create the context for the template
    context = {
        'title': 'Page not found',
        'url': request.base_url,
    }

    # Render the 404.html template with the context and return with status code 404
    return render_template('404.html', **context), 404


if __name__ == '__main__':
    app.run(debug=True)
