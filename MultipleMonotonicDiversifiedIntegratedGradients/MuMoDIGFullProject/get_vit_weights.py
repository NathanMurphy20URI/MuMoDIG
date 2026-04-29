import timm
import torch

models = {
    "coat_tiny":                    "coat_tiny",
    "deit_small_patch16_224":       "deit_small_patch16_224",
    "deit_tiny_patch16_224":        "deit_tiny_patch16_224",
    "pit_b_224":                    "pit_b_224",
    "pit_ti_224":                   "pit_ti_224",
    "swin_small_patch4_window7_224":"swin_small_patch4_window7_224",
    "swin_tiny_patch4_window7_224": "swin_tiny_patch4_window7_224",
    "visformer_small":              "visformer_small",
    "visformer_tiny":               "visformer_tiny",
    "vit_base_patch16_224":         "vit_base_patch16_224",
}

for name, model_name in models.items():
    model = timm.create_model(model_name, pretrained=True)
    # Save as .bin (HuggingFace format)
    torch.save(model.state_dict(), f"./vit_weight/{name}.bin")
    print(f"Saved {name}.bin")