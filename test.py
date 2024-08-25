from llama_cpp import Llama
import json

def call_chat_completion (topic="The Impact of Social Media on Mental Health", essay="Social media has become an integral part of our daily lives, connecting us with friends, family, and the wider world. While these platforms offer numerous benefits, such as facilitating communication and access to information, their impact on mental health is a growing concern. Studies have shown a correlation between excessive social media use and increased levels of anxiety, depression, and low self-esteem. The constant comparison to others, the fear of missing out (FOMO), and the curated portrayals of seemingly perfect lives can contribute to feelings of inadequacy and dissatisfaction. Additionally, cyberbullying and online harassment can have severe consequences for mental well-being. It is important to recognize these potential risks and develop healthy habits around social media use, such as setting limits on screen time, prioritizing real-life interactions, and seeking support if needed."):
    llm = Llama(
        model_path="model/llama-2-7b-chat.Q4_K_M.gguf",
        n_gpu_layers=-1, # Uncomment to use GPU acceleration
        # seed=1337, # Uncomment to set a specific seed
        # n_batch=32,
        n_ctx=1700, # Uncomment to increase the context window
        split_mode=2,
    )

    output = llm('''
[INST]

<<SYS>> Rate each essay under the two categories by how relevant it is to the topic asked: "Not Relevant" and "Relevant".

Provide feedback on how to make the essay more relevant to the topic asked or instruction given. Finally, provide detailed and constructive feedback on how to make the essay better generally. These are the explanations of these ratings:

"Not Relevant" means the content of the essay was mostly not relevant to the topic asked and instruction given.

"Relevant" means the content of the essay was mostly relevant to the topic asked and instruction given.

<</SYS>>

What is the relevance rating of the following essay to the topic "The History of Ancient Rome"? essay:
The development of modern computer technology has revolutionized various aspects of human life. From communication to transportation, education to entertainment, computers have become integral to our daily activities. With the advent of the internet, information is readily accessible at our fingertips, allowing for unprecedented connectivity and knowledge sharing. Moreover, advancements in artificial intelligence and machine learning are transforming industries such as healthcare, finance, and manufacturing. As we continue to innovate and harness the power of technology, the possibilities for progress and development are endless. 

[/INST]
Rating: "Not Relevant", Feedback: "The essay discusses the impact of computer technology, which is irrelevant to the topic of the history of Ancient Rome. The discussion about modern computer technology, while interesting, does not contribute to the exploration of Ancient Rome's history. To make the essay more relevant, focus on discussing key events, figures, and developments in Ancient Rome, providing historical context and significance. In addition, the essay should delve into the political, social, and cultural aspects of Ancient Rome, highlighting societal structures that shaped its development and legacy to enhance relevance. This would provide a more cohesive and aligned focus with the topic at hand."

[INST]What is the relevance rating of the following essay to the topic "Strategies for Effective Communication in the Workplace"? essay:
Effective communication is essential for fostering collaboration, building trust, and achieving common goals in the workplace. Clear and concise communication helps to prevent misunderstandings, conflicts, and inefficiencies, promoting a positive work environment and organizational success. Strategies for improving communication in the workplace include active listening, asking clarifying questions, providing constructive feedback, and choosing the appropriate communication channels. Additionally, fostering open communication channels, promoting transparency, and encouraging feedback and dialogue contribute to a culture of communication excellence. By investing in communication skills training and creating a supportive communication environment, organizations can enhance productivity, employee satisfaction, and overall performance.
[/INST]
Rating: "Relevant", Feedback: "The essay discusses strategies for effective communication in the workplace, which is completely relevant to the topic. It provides valuable insights into the importance of communication skills and practical tips for enhancing communication effectiveness in a professional setting or workplace, aligning perfectly with the topic. It further emphasizes the importance of strategies such as active listening, fostering open communication channels, and promoting transparency, all of which contribute to a culture of communication excellence. This focus on actionable steps to enhance communication effectiveness underscores its relevance to workplace dynamics and organizational success."

[INST]What is the relevance rating of the following essay to the topic "What are the benefits of organic farming?"? essay:
The exploration of outer space has been a remarkable achievement for humanity, pushing the boundaries of our understanding and knowledge of the universe. Space missions have allowed us to explore distant planets, moons, and celestial bodies, uncovering new insights into the origins and evolution of our solar system. Moreover, space exploration has led to the development of innovative technologies and scientific advancements that benefit various fields, from medicine to telecommunications. As we continue to explore the cosmos, we expand our horizons and inspire future generations to pursue scientific discovery and exploration.
[/INST]
Rating: "Not Relevant", Feedback: "The essay discusses space exploration, which is unrelated to the topic of the benefits of organic farming. To improve relevance, focus on discussing the advantages of organic farming practices, such as environmental sustainability, improved soil health, and reduced chemical exposure. This would ensure that the essay aligns with the topic and provides insights into the benefits of organic farming for agriculture and the environment."

[INST]What is the relevance rating of the following essay to the topic "Talk about the benefits of a balanced diet and regular exercise"? essay:
A balanced diet and regular exercise are fundamental components of a healthy lifestyle, contributing to overall well-being and disease prevention. A balanced diet provides essential nutrients, vitamins, and minerals necessary for optimal bodily function, growth, and repair. Incorporating a variety of fruits, vegetables, whole grains, lean proteins, and healthy fats into one's diet supports energy levels, cognitive function, and immune health. Regular exercise improves cardiovascular health, muscle strength, flexibility, and endurance, reducing the risk of chronic diseases such as obesity, diabetes, and heart disease. Moreover, exercise releases endorphins, neurotransmitters that promote feelings of happiness and well-being, reducing stress and anxiety levels. By prioritizing a balanced diet and regular exercise, individuals can enjoy better physical health, mental well-being, and quality of life.
[/INST]
Rating: "Relevant", Feedback: "The essay discusses the benefits of a balanced diet and regular exercise, which is completely relevant to the topic. It provides comprehensive information on the importance of nutrition and physical activity for maintaining overall health and well-being. By emphasizing the contributions of a balanced diet and regular exercise to optimal bodily function, disease prevention, and mental well-being, the essay effectively aligns with the topic's focus on promoting healthy lifestyle choices."

[INST]What is the relevance rating of the following essay to the topic "'''+topic+'''"? essay:
'''+essay+'''
[/INST]                                   
    ''',
            # max_tokens=5
            # stop=["\n"],
            
            
    )
    return json.dumps(output)
