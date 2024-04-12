from diffusers import DiffusionPipeline

if __name__ == '__main__':
    # 用from_pretrained()方法加载模型 SD
    pipeline = DiffusionPipeline.from_pretrained("runwayml/stable-diffusion-v1-5")
    # print(pipeline)
    # DiffusionPipeline会下载并缓存所有的建模、标记化和调度组件。你可以看到StableDiffusion的pipeline是由UNet2DConditionModel和PNDMScheduler等组件组成的：
    image = pipeline("superman").images[0]
    image.save("superman.png")