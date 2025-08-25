# UserService

UserService is a Python FastAPI application designed to...

## Features
- TODO

## Prerequisites
- [UV](https://docs.astral.sh/uv/getting-started/installation/#__tabbed_1_2): Modern Python Package Manager

## Getting Started

### Clone the Repository
```bash
git clone https://github.com/Agile-Software-Engineering-25/team-9-backend-stammdaten-studieneinheiten.git
cd team-9-backend-stammdaten-studieneinheiten
```

### Install Dependencies
```bash
uv sync
```

### Run the Service
If it did't happen automatically already, activate the virtual environment (Indicated by the environment name in brackets before the path in your shell):
#### Windows
```powershell
PS> .venv\Scripts\activate
```
#### Linux and macOS
```bash
source .venv/bin/activate
```

Now run the service:
```bash
uvicorn app.main:app --reload
```
The service is available on Port 8000 by default. Use the `--port` option to specify a different port.

FastAPI automatically generates a Swagger Documentation under `/docs/`

## Testing
### Unit Tests
TODO

## Code Style & Linting
If you are using VS-Code as your text editor of choice, you can install the following extensions to make development easier:
- [Ruff](https://marketplace.visualstudio.com/items?itemName=charliermarsh.ruff)

### Settings for Ruff linter
You can configure special settings for your workspace in VS-Code with a `.vscode/settings.json` file. Add the following contents to that file:
```json
{
  "[python]": {
    "editor.formatOnSave": true,
    "editor.defaultFormatter": "charliermarsh.ruff",
  }
}
```

## Resources
- [FastAPI Documentation](https://fastapi.tiangolo.com/learn/)
- [UV Documentation](https://docs.astral.sh/uv/)
