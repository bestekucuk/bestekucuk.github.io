from flask_restx import Resource, Namespace, reqparse

from .model import classify


ns = Namespace("api")

@ns.route("/your_endpoint")
class YourResource(Resource):
    def get(self):
        return {"message": "Hello, World!"}

@ns.route("/hello")
class Hello(Resource):
    def get(self):
        return {"hello": "restx"}
    

# Örnek kategori listesi
available_categories = ["Category1", "Category2", "Category3"]

# Derin öğrenme modelini yükleyen fonksiyon
def load_deep_learning_model():
    # Burada gerçek modelin yüklenmesi gerekir
    # Model yükleme işlemi modelin türüne ve kullanılan kütüphaneye bağlı olarak değişebilir
    # Örneğin, TensorFlow, PyTorch, Hugging Face Transformers vb.
    # Yüklenen modeli döndür
    return None  # Gerçek modeli döndürmek gerekir

# Metni kategoriye sınıflandıran fonksiyon
def classify_text(model, text):
    # Gerçek bir sınıflandırma işlemi yapılmalıdır
    # Bu örnek sınıflandırma fonksiyonu, modelin olmadığını ve gerçek bir sınıflandırma fonksiyonu kullanmanız gerektiğini belirtir
    return "Unclassified"  

# Metin analizi için kullanılacak parser
text = reqparse.RequestParser()
text.add_argument("text", type=str, required=True, help="Text to classify")

@ns.route("/classify")
class TextClassificationAPI(Resource):
    def get(self):
        return {"text": "text" ,"category": "category"}
    
    @ns.expect(text)  
    def post(self):
        # Metin verisini al
        args = text.parse_args()
        text_to_classify = args["text"]

        # Derin öğrenme modelini yükle
        #deep_learning_model = load_deep_learning_model()

        #f deep_learning_model is not None:
            # Metni sınıflandır
        category = classify(text_to_classify)

            # Sonucu döndür
        return {"text": text_to_classify, "category": category}



text_parser = reqparse.RequestParser()
text_parser.add_argument("text", type=str, required=True, help="Text to process")

@ns.route("/process_text")
class TextProcessingAPI(Resource):
    @ns.expect(text_parser)
    def post(self):
        args = text_parser.parse_args()
        text_to_process = args["text"]

        # Burada metin verisini kullanarak istediğiniz işlemleri gerçekleştirebilirsiniz
        # Örneğin, metni büyük harfe çevirelim
        processed_text = text_to_process.upper()

        return { "category": processed_text}, 200