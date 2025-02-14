
items =["one","one"]
items.append("one")
print(items.count("one"))

class Car:
    pass

audi = Car()
print(type(audi))

import nltk
speech = """ I have three visions for India. In 3000 years of our history people from all over the world have come and invaded us, captured our lands, conquered our minds. From Alexander onwards the Greeks, the Turks, the Moguls, the Portuguese, the British, the French, the Dutch, all of them came and looted us, took over what was ours. Yet we have not done this to any other nation. We have not conquered anyone. We have not grabbed their land, their culture and their history and tried to enforce our way of life on them. Why? Because we respect the freedom of others. That is why my FIRST VISION is that of FREEDOM. I believe that India got its first vision of this in 1857, when we started the war of Independence. It is this freedom that we must protect and nurture and build on. If we are not free, no one will respect us.

We have 10 percent growth rate in most areas. Our poverty levels are falling. Our achievements are being globally recognised today. Yet we lack the self-confidence to see ourselves as a developed nation, self-reliant and self-assured. Isn’t this incorrect? MY SECOND VISION for India is DEVELOPMENT. For fifty years we have been a developing nation. It is time we see ourselves as a developed nation. We are among top five nations in the world in terms of GDP."""
sentence = """The Eiffel Tower was built from 1887 to 1889 by French engineer Gistave Eiffel,0 
whose company specialized in building etal frameworks and structures."""

# sentences = nltk.sent_tokenize(speech)
# nltk.download('words')
# nltk.download('maxent_ne_chunker_tab')
# words = [nltk.word_tokenize(sent) for sent in sentences ]
# print(words)
# tagged_element = [nltk.pos_tag(word) for word in words ]
# chunked_element = nltk.ne_chunk(tagged_element)
# chunked_element.draw()

words = nltk.word_tokenize(speech)
tagged = nltk.pos_tag(words)
nltk.ne_chunk(tagged).draw()