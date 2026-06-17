from app import create_app, db
from app.models import User, File, AuditLog
from config import Config

# Create app at module level (required for Vercel)
app = create_app()

@app.shell_context_processor
def make_shell_context():
    return {
        'db': db,
        'User': User,
        'File': File,
        'AuditLog': AuditLog
    }

if __name__ == '__main__':
    import os
    host = os.environ.get('SERVER_HOST', '0.0.0.0')
    port = int(os.environ.get('PORT', os.environ.get('SERVER_PORT', 5000)))
    debug = os.environ.get('FLASK_ENV') != 'production'
    print(f'\n🚀 Secure File Vault is running at: {Config.BASE_URL}\n')
    print(f'Share this URL with others: {Config.BASE_URL}\n')
    app.run(debug=debug, host=host, port=port, threaded=True)