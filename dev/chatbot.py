"""
RAGシステムによるチャットボット
事前に用意した文書群からユーザーの関心に近い文書を引き出して、文章生成AIに回答を生成させる
"""
class Chatbot():

    """
    RAGシステムの起動に失敗した場合はthrowし、システムの一切をクラッシュする
    @param doc_path 検索文書フォルダの名前
    @param ebd_name 埋め込みモデルの名前（huggingfaceリポジトリに準拠）
    @param llm_name LLMモデルの名前（huggingfaceリポジトリに準拠）
    @param tkn_name トークナイザーモデルの名前（huggingfaceリポジトリに準拠）
    """
    def __init__(
        self,
        doc_path: str,
        ebd_name: str,
        llm_name: str,
        tkn_name: str = ""
    ) -> None:
        ## 検索文書のロード
        ## RAG検索系の起動
        ## LLMおよびトークナイザーのロード
        ## 文章生成パイプラインの起動
        pass
    
    """
    チャットボットが問い合わせに答える
    チャットボットが文章の生成に失敗した場合でも、システムはクラッシュせずthrowするだけ
    @param query 問い合わせ文章
    @return チャットボットが考えた文章
    """
    def generate_sentence(
        self,
        query: str
    ) -> str:
        pass
        