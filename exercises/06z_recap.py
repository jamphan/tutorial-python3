# ========================================================================================================

# Copy and paste these three variables
STOP_WORDS = ["i", "me", "my", "myself", "we", "our", "ours", "ourselves", "you", "your", "yours", "yourself", "yourselves", "he", "him", "his", "himself", "she", "her", "hers", "herself", "it", "its", "itself", "they", "them", "their", "theirs", "themselves", "what", "which", "who", "whom", "this", "that", "these", "those", "am", "is", "are", "was", "were", "be", "been", "being", "have", "has", "had", "having", "do", "does", "did", "doing", "a", "an", "the", "and", "but", "if", "or", "because", "as", "until", "while", "of", "at", "by", "for", "with", "about", "against", "between", "into", "through", "during", "before", "after", "above", "below", "to", "from", "up", "down", "in", "out", "on", "off", "over", "under", "again", "further", "then", "once", "here", "there", "when", "where", "why", "how", "all", "any", "both", "each", "few", "more", "most", "other", "some", "such", "no", "nor", "not", "only", "own", "same", "so", "than", "too", "very", "s", "t", "can", "will", "just", "don", "should", "now"]

SPECIAL_CHARACTERS = ".,!@#$%^&*()_+';:[]-?"

bill_gates_tweets = [
    "@StephenCurry30’s work in the community is as inspiring as his amazing record on the basketball court. I really appreciated the thoughtful conversation.",
    "Dr. Tunji Funsho’s work with @Rotary was essential in stopping wild polio in Africa and will help create a polio-free world for all. A well-deserved recognition.",
    "This honor is well deserved. COVID-19 is not just a health crisis—it is also now a food crisis, and @WFP is there to respond. I’m inspired by the thousands of people in the organization who have committed their lives to fighting hunger.",
    "For the last 25 years, Dr. Firdausi Qadri, an immunologist and infectious disease researcher in Bangladesh, has been working to protect entire communities from cholera epidemics.",
    "I’m excited to see this kind of innovation. Detecting and predicting outbreaks earlier is critical to preventing epidemics.",
    "The only way to eliminate the threat of COVID-19 somewhere is to eliminate it everywhere. By making sure poor countries are equipped to stop this disease, wealthy countries will help themselves and bring this crisis to an end sooner.",
    "Understanding this concept can help us measure our progress toward eliminating carbon emissions and serve as a guide to action.",
    "Developing and manufacturing vaccines won’t end the pandemic quickly unless we also deliver them equitably. Here is why it’s critical that vaccines are distributed in proportion to the global population: https://b-gat.es/3468JHV",
    "Great to see the UK commit vital funding to ensure COVID-19 vaccines are available for the world’s poorest people. PM @BorisJohnson's plan will improve the way we prepare for future crises like this.",
    "What do COVID-19 and malaria have to do with each other? When COVID-19 struck, it disrupted the entire global health care system—including the fight against malaria.",
    "After 20 years of stunning advances toward global goals to improve health and reduce poverty, the COVID-19 pandemic stopped progress in its tracks. In our foundation’s Goalkeepers report, we survey the damage and discuss how to start reversing it.",
    "To prevent the worst effects of climate change, we need innovation across all sectors—especially in the hardest to decarbonize sectors—to get us on a viable path to net-zero emissions.",
    "Dr. John Nkengasong is a true Goalkeeper. His leadership will help ensure Africa has the tools it needs to fight COVID-19: https://b-gat.es/367MvYZ",
]

# ========================================================================================================

# Type the rest!

all_words, word_count = [], []

for tweet in bill_gates_tweets:

    # Clean up the tweet before doing analysis
    preproc_tweet = tweet.strip().lower()
    for special_char in SPECIAL_CHARACTERS:
        preproc_tweet = preproc_tweet.replace(special_char, '')

    # Split the sentence into words
    split_sentence = preproc_tweet.split(' ')

    # For every word in the sentence...
    for word in split_sentence:

        # If the word is a stop word, ignore it
        if word in STOP_WORDS:
            continue

        # Else if the word is not currently tracked, add it
        elif word not in all_words:
            all_words.append(word)
            word_count.append(1)

        # Else if we already track it, add to the tracker
        else:
            word_idx = all_words.index(word)
            word_count[word_idx] += 1

# Print all of the unique words that are used more than twice and their counts
print(f"\n{'='*80}\nWords that Bill Gate's used more than twice\n{'='*80}")
for n, word in zip(word_count, all_words):
    if n > 2:
        print(f"\t{word.title(): <50}: Used {n} times")

# Find the most used word
print('='*80)
top_word_count = max(word_count)
most_used_word_idx = word_count.index(top_word_count)
most_used_word = all_words[most_used_word_idx]
print(f"Bill Gate's most used word is: {most_used_word.title()}, used {top_word_count} times\n")
