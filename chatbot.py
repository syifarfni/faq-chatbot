from transformers import AutoModelForCausalLM, AutoTokenizer

model_name = "Qwen/Qwen2.5-1.5B-Instruct"
print("loading... harap menunggu ya!")

tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(
    model_name,
    torch_dtype="auto",
    device_map="auto"
)

print("Model berhasil dimuat!")

# baca faq
with open("faq.txt", "r", encoding="utf-8") as file:
    faq_context = file.read()

print ("\n=== Chatbot Sharing Seputar Kehidupan Mahasiswa ===")
print ("ketik 'keluar' untuk mengakhiri.\n")

while True:
    user_question = input("Anda: ")
    if user_question.lower()=="keluar":
        print("Bot : Sampai Jumpa!")
        break

    messages = [
        {
            "role" : "system",
            "content" : f"""
berikut adalah FAQ:

{faq_context}
Instruksi:
- Jawab hanya berdasarkan konteks FAQ di atas.
- Jangan menambahkan informasi yang tidak ada pada FAQ.
- Jika jawaban tidak ditemukan dalam FAQ, jawab:
'Maaf, saya tidak dapat membantu pertanyaan tersebut. Silakan berikan pertanyaan seputar kehidupan mahasiswa.'
"""
        },

        {
            "role" : "user",
            "content" : user_question
        }
    ]

    text = tokenizer.apply_chat_template(
        messages,
        tokenize=False,
        add_generation_prompt=True,
    )
    model_inputs = tokenizer([text], return_tensors="pt").to(model.device)

    # conduct text completion
    generated_ids = model.generate(
        **model_inputs,
        max_new_tokens=100
    )
    output_ids = generated_ids[0][len(model_inputs.input_ids[0]):].tolist() 

    content = tokenizer.decode(output_ids, skip_special_tokens=True)

    print("Bot:", content)
