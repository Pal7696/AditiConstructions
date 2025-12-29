def handler(event, context):
    from werkzeug.wrappers import Request
    from werkzeug.serving import run_simple
    
    # Create a WSGI application
    return app

# For local development
if __name__ == '__main__':
    app.run(debug=True)
=======
# For Vercel deployment, the app object is the handler
# For local development
if __name__ == '__main__':
    app.run(debug=True)
