"""
handles streaming content over to client
"""

def template(app ,template_name, **context):
    """
    override flask's jinja to support streaming data
    to template
    """
    app.update_template_context(context)
    t = app.jinja_env.get_template(template_name)
    rv = t.stream(context)
    rv.enable_buffering(5)
    return rv
