import warnings
import numpy as np
from datetime import date
from ....base import catch_vector_errors
from ....doc_utils import ModelDefinition
from ....import_utils import is_all_dependency_installed
from ....models_dict import MODEL_REQUIREMENTS
from ..base import BaseText2Vec
from .use import USE2Vec

if is_all_dependency_installed(MODEL_REQUIREMENTS['encoders-text-tfhub-use-multi']):
    import tensorflow as tf
    import tensorflow_text

USEMultiModelDefinition = ModelDefinition(markdown_filepath='encoders/text/tfhub/use_multi')

__doc__ = USEMultiModelDefinition.create_docs()

class USEMulti2Vec(USE2Vec):
    definition = USEMultiModelDefinition
    def __init__(self, model_url: str = 'https://tfhub.dev/google/universal-sentence-encoder-multilingual/3'):
        list_of_urls = [
            "https://tfhub.dev/google/universal-sentence-encoder-multilingual/3",
            "https://tfhub.dev/google/universal-sentence-encoder-multilingual-large/3",
        ]
        self.validate_model_url(model_url, list_of_urls)
        self.init(model_url)
        self.vector_length = 512
