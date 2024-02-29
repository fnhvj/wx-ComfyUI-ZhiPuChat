from zhipuai import ZhipuAI
class ZhiPuChat:
    def __init__(self):
        pass
    
    @classmethod
    def INPUT_TYPES(s):
 
        return {
            "required": {
                "api_key": ("STRING", {
                    "multiline": False,
                    "default": "pleace input your api_key"
                }),
                "model": (['glm-4', 'glm-3-turbo', 'characterglm'], {'default': 'glm-4'}),
                "question": ("STRING", {
                    "multiline": True,
                    "default": ""
                }),
            },
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("STRING",)

    FUNCTION = "zhipuchat"

    # OUTPUT_NODE = False

    CATEGORY = "ZhiPuChat"

    def zhipuchat(self, question,api_key,model):
        if question=="" or api_key=="":
            return ("你没有填写api_key",)
        if question=="":
            return ("没有收到你的问题",)
        self.client = ZhipuAI(api_key=api_key)
        answer = ""
        response = self.client.chat.completions.create(
            model=model,  # 填写需要调用的模型名称
            messages=[
                {"role": "user", "content": question},
            ],
        )
        print(response.choices[0].message.content)
        answer = response.choices[0].message.content if response else answer
        return (answer,)

NODE_CLASS_MAPPINGS = {
    "ZhiPuChat": ZhiPuChat
}

# A dictionary that contains the friendly/humanly readable titles for the nodes
NODE_DISPLAY_NAME_MAPPINGS = {
    "ZhiPuChat": "ZhiPuChatNode"
}
