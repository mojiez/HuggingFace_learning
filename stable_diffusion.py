from diffusers import DiffusionPipeline

if __name__ == '__main__':
    # 用from_pretrained()方法加载模型。
    pipeline = DiffusionPipeline.from_pretrained("runwayml/stable-diffusion-v1-5")
    print(pipeline)
