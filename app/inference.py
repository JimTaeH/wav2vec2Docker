from transformers import Wav2Vec2Processor
from transformers import Wav2Vec2ForCTC
import torch

processor = Wav2Vec2Processor.from_pretrained("/wav2vec2/processor/")
model = Wav2Vec2ForCTC.from_pretrained("/wav2vec2/model129hrs/",
                                    attention_dropout=0.1,
                                    hidden_dropout=0.1,
                                    feat_proj_dropout=0.0,
                                    mask_time_prob=0.05,
                                    layerdrop=0.1,
                                    ctc_loss_reduction="mean",
                                    pad_token_id=processor.tokenizer.pad_token_id,
                                    vocab_size=len(processor.tokenizer))

device = "cuda" if torch.cuda.is_available() else "cpu"
model.to(device)

def stt(audioData=None, sr=None):
    input_values = processor(audioData, sampling_rate=sr, return_tensors="pt").input_values
    
    with torch.no_grad():
        logits = model(input_values[0].to(device)).logits

    predicted_ids = torch.argmax(logits, dim=-1)
    text = processor.batch_decode(predicted_ids)[0]

    return text