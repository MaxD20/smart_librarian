import json
import os

txt_out = os.path.join("data", "book_summaries.txt")
dict_out = os.path.join("data", "book_summaries_dict.json")

summaries = {
    "1984": (
        "A dystopian story about a totalitarian society controlled by surveillance, propaganda, and thought police. "
        "Winston Smith secretly rebels in search of truth and freedom."
    ),
    "The Hobbit": (
        "Bilbo Baggins, a comfort-loving hobbit, is pulled into a quest to reclaim a stolen treasure guarded by a dragon. "
        "He discovers courage, loyalty, and adventure in a world of mythical creatures."
    ),
    "To Kill a Mockingbird": (
        "Set in the American South during the 1930s, this novel explores themes of racial injustice and moral growth "
        "through the eyes of young Scout Finch, whose father Atticus defends a Black man falsely accused of rape."
    ),
    "Pride and Prejudice": (
        "Elizabeth Bennet navigates issues of class, marriage, and personal misunderstandings in 19th-century England. "
        "Her sharp wit and strong will make her a memorable literary heroine."
    ),
    "The Great Gatsby": (
        "A portrayal of the American Dream and the moral decay of the 1920s. "
        "Jay Gatsby’s obsession with wealth and Daisy Buchanan leads to inevitable tragedy."
    ),
    "Harry Potter and the Sorcerer's Stone": (
        "An orphan discovers he is a wizard and begins his magical education at Hogwarts. "
        "Alongside new friends, he uncovers secrets about his parents' past and a dark wizard seeking immortality."
    ),
    "The Catcher in the Rye": (
        "Holden Caulfield recounts a few days of his life in New York City after being expelled from prep school. "
        "The novel explores themes of teenage alienation and existential angst."
    ),
    "Brave New World": (
        "In a futuristic society driven by technology and instant gratification, individuals are conditioned to conform. "
        "Bernard Marx seeks meaning in a world where happiness is manufactured and individuality is suppressed."
    ),
    "Moby Dick": (
        "Captain Ahab obsessively hunts the white whale, Moby Dick, on a doomed voyage. "
        "The novel explores themes of obsession, revenge, and humanity's struggle with nature."
    ),
    "The Alchemist": (
        "Santiago, a young shepherd, dreams of finding treasure in Egypt. "
        "His journey becomes a spiritual quest about fulfilling one’s destiny and listening to the heart."
    ),
    "The Lord of the Rings: The Fellowship of the Ring": (
        "Frodo Baggins inherits a powerful ring and sets out on a perilous journey to destroy it. "
        "A fellowship forms to help him navigate threats across Middle-earth."
    ),
    "Jane Eyre": (
        "An orphaned girl becomes a governess and falls in love with her employer, Mr. Rochester. "
        "Dark secrets threaten their relationship as she seeks independence and self-respect."
    ),
    "Frankenstein": (
        "Victor Frankenstein creates a living being from dead tissue, only to be horrified by his creation. "
        "The novel raises questions about scientific ethics and human responsibility."
    ),
    "Crime and Punishment": (
        "Raskolnikov, a poor student in St. Petersburg, believes he's above moral law and commits murder. "
        "The psychological drama explores guilt, redemption, and justice."
    ),
    "Wuthering Heights": (
        "A dark romance between Heathcliff and Catherine Earnshaw spans generations. "
        "Set on the moors, the story is full of passion, revenge, and haunting memories."
    ),
    "Animal Farm": (
        "A group of farm animals overthrow their human owner to create an equal society, "
        "only to watch it devolve into a dictatorship. An allegory of the Russian Revolution."
    ),
    "Dracula": (
        "Jonathan Harker encounters Count Dracula, a vampire seeking to move from Transylvania to England. "
        "A band of friends unite to battle the growing darkness."
    ),
    "The Picture of Dorian Gray": (
        "Dorian Gray remains youthful while his portrait ages, reflecting his moral corruption. "
        "A cautionary tale of vanity, indulgence, and consequence."
    ),
    "The Chronicles of Narnia: The Lion, the Witch and the Wardrobe": (
        "Four siblings discover a magical land ruled by a tyrannical witch. "
        "They join forces with the lion Aslan to bring peace to Narnia."
    ),
    "Fahrenheit 451": (
        "In a future where books are banned, fireman Guy Montag burns them for a living. "
        "After meeting a free-thinking girl, he begins to question everything."
    ),
    "The Hunger Games": (
        "In a dystopian future, Katniss Everdeen volunteers to take her sister's place in a deadly televised competition. "
        "She must rely on her instincts and cunning to survive the brutal Hunger Games."
    ),
    "The Giver": (
        "Jonas lives in a seemingly perfect society without pain or choice. "
        "When he is chosen to receive memories of the past, he discovers dark truths about his world."
    ),
    "Little Women": (
        "The story of the March sisters—Meg, Jo, Beth, and Amy—as they grow up during the Civil War. "
        "It explores themes of family, ambition, and womanhood."
    ),
    "The Secret Garden": (
        "Mary Lennox discovers a hidden, neglected garden on her uncle’s estate and brings it back to life. "
        "The story is one of healing, friendship, and renewal."
    ),
    "The Kite Runner": (
        "Amir, a boy from Kabul, reflects on his betrayal of a loyal friend and seeks redemption. "
        "A powerful tale of friendship, guilt, and the scars of war."
    ),
    "Life of Pi": (
        "After a shipwreck, young Pi Patel is stranded on a lifeboat with a Bengal tiger. "
        "His journey becomes one of survival, faith, and imagination."
    ),
    "A Tale of Two Cities": (
        "Set during the French Revolution, the novel contrasts the cities of London and Paris. "
        "Themes include sacrifice, justice, and resurrection."
    ),
    "Great Expectations": (
        "Pip, a poor orphan, navigates class, ambition, and love after receiving an unexpected fortune. "
        "A story of personal growth and moral development."
    ),
    "Emma": (
        "Emma Woodhouse is a wealthy young woman who fancies herself a matchmaker. "
        "Her misguided meddling leads to romantic complications and self-discovery."
    ),
    "Don Quixote": (
        "An aging man becomes a self-declared knight and sets out on absurd adventures with his loyal squire. "
        "A satirical exploration of idealism and reality."
    ),
    "Les Misérables": (
        "Jean Valjean, a former convict, seeks redemption while being pursued by Inspector Javert. "
        "The story spans revolution, love, and justice in 19th-century France."
    ),
    "The Count of Monte Cristo": (
        "Wrongfully imprisoned, Edmond Dantès escapes and plots his revenge. "
        "A tale of betrayal, transformation, and retribution."
    ),
    "The Odyssey": (
        "Homer’s epic poem follows Odysseus as he journeys home from the Trojan War, facing mythical creatures and divine wrath."
    ),
    "Beowulf": (
        "An ancient hero fights monsters and dragons to protect his people. "
        "Themes of bravery, loyalty, and legacy dominate this Old English epic."
    ),
    "Dr. Jekyll and Mr. Hyde": (
        "Dr. Jekyll’s experiments unleash his violent alter ego, Mr. Hyde. "
        "A psychological thriller about duality and the nature of evil."
    ),
    "Treasure Island": (
        "Young Jim Hawkins sets off on a sea voyage in search of pirate treasure. "
        "The classic adventure explores greed, courage, and betrayal."
    ),
    "The Adventures of Huckleberry Finn": (
        "Huck Finn escapes an abusive father and travels down the Mississippi River with a runaway slave. "
        "A critique of racism and society in pre-Civil War America."
    ),
    "The Time Machine": (
        "A scientist travels far into the future and discovers the fate of humanity. "
        "H.G. Wells explores class division, progress, and decay."
    ),
    "Around the World in 80 Days": (
        "Phileas Fogg wagers he can circumnavigate the globe in 80 days. "
        "A fast-paced adventure full of unexpected challenges and encounters."
    ),
    "Anne of Green Gables": (
        "Anne Shirley, a spirited orphan, is adopted by siblings on Prince Edward Island. "
        "Her imagination and curiosity bring joy and chaos to their quiet lives."
    )
}

with open(txt_out, "w", encoding="utf-8") as f_txt:
    for title, summary in summaries.items():
        f_txt.write(f"## Title: {title}::{summary.strip()}\n")

with open(dict_out, "w", encoding="utf-8") as f_json:
    json.dump(summaries, f_json, indent=2, ensure_ascii=False)

