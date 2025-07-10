# =============================================================================
# config/settings.py - Configuration management
# =============================================================================

from pydantic import BaseSettings
from typing import Dict, Optional
import os

class Settings(BaseSettings):
    # Server settings
    port: int = 8000
    host: str = "0.0.0.0"
    debug: bool = False
    
    # API Keys
    openai_api_key: Optional[str] = None
    anthropic_api_key: Optional[str] = None
    google_api_key: Optional[str] = None
    
    # Model settings
    default_temperature: float = 0.7
    max_tokens: int = 2000
    
    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # Load from environment variables if not provided
        self.openai_api_key = self.openai_api_key or os.getenv("OPENAI_API_KEY")
        self.anthropic_api_key = self.anthropic_api_key or os.getenv("ANTHROPIC_API_KEY")
        self.google_api_key = self.google_api_key or os.getenv("GOOGLE_API_KEY")
    
    @property
    def api_keys(self) -> Dict[str, Optional[str]]:
        return {
            "openai": self.openai_api_key,
            "anthropic": self.anthropic_api_key,
            "google": self.google_api_key,
        }

# Singleton pattern for settings
_settings = None

def get_settings() -> Settings:
    global _settings
    if _settings is None:
        _settings = Settings()
    return _settings