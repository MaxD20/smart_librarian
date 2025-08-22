from pathlib import Path
import json

project_root = Path(__file__).resolve().parents[1]  # .../smart_librarian
out_dir = project_root / "data"
out_dir.mkdir(parents=True, exist_ok=True)

txt_out = out_dir / "book_summaries.txt"
dict_out = out_dir / "book_summaries_dict.json"


book_summaries_dict = {
    "1984": {
        "short": "A dystopian story about a totalitarian society controlled by surveillance, propaganda, and thought police. "
        "Winston Smith secretly rebels in search of truth and freedom.",
        "full": (
            "George Orwell depicts a brutal one-party state that rewrites history and polices thought itself. "
            "Winston Smith, a clerk at the Ministry of Truth, begins a doomed love affair "
            "with Julia and keeps a secret diary as acts of rebellion. "
            "Captured by the Thought Police, he is tortured into betraying Julia and accepting the Party's reality. "
            "The novel dissects propaganda, language control, and the fragility of individual freedom.\n"
            "Big Brother’s omnipresent gaze ensures conformity, while Newspeak limits the range of thought. "
            "Winston’s struggle is both personal and political, reflecting the dangers of unchecked authority. "
            "The bleak ending underscores the loss of individuality and hope in a repressive regime."
        ),
        "themes": [
            "dystopia",
            "totalitarianism",
            "surveillance",
            "propaganda",
            "freedom",
            "rebellion",
        ],
    },
    "The Hobbit": {
        "short": "Bilbo Baggins, a comfort-loving hobbit, is pulled "
        "into a quest to reclaim a stolen treasure guarded by a dragon."
        " He discovers courage, loyalty, and adventure in a world of mythical creatures.",
        "full": (
            "Bilbo Baggins is recruited by Gandalf and a band of dwarves to reclaim Erebor from the dragon Smaug. "
            "On the journey he survives trolls, goblins, spiders, and wood-elves, and wins a mysterious ring from Gollum. "
            "Bilbo’s stealth and cleverness repeatedly save the company and reshape his sense of self. "
            "The adventure culminates in the Battle of Five Armies and Bilbo’s return home, forever changed.\n"
            "Bilbo’s transformation from reluctant participant to clever hero is central to the story. "
            "The novel introduces Middle-earth and sets the stage for Tolkien’s later works. "
            "Themes of home, bravery, and the unexpected value of ordinary people are woven throughout."
        ),
        "themes": ["adventure", "friendship", "courage", "quest", "fantasy"],
    },
    "To Kill a Mockingbird": {
        "short": "Set in the American South during the 1930s, this novel explores themes of racial injustice and moral growth "
        "through the eyes of young Scout Finch, whose father Atticus "
        "defends a Black man falsely accused of rape.",
        "full": (
            "Scout Finch grows up in Maycomb, Alabama, witnessing her father Atticus defend Tom Robinson, a Black man wrongly accused of raping a white woman. "
            "Through her childhood adventures and observations, Scout learns about prejudice, empathy, and the complexities of human nature. "
            "The trial and its aftermath expose the deep-seated racism of the community, shaping Scout’s understanding of justice and morality.\n"
            "Atticus Finch’s unwavering integrity serves as a moral compass for his children and the town. "
            "The mysterious neighbor Boo Radley becomes a symbol of misunderstood kindness. "
            "Harper Lee’s novel remains a powerful critique of social injustice and the loss of innocence."
        ),
        "themes": ["racism", "justice", "childhood", "morality", "coming of age"],
    },
    "Pride and Prejudice": {
        "short": "Elizabeth Bennet navigates issues of class, marriage, and personal misunderstandings in 19th-century England. Her sharp wit and strong will make her a memorable literary heroine.",
        "full": (
            "Elizabeth Bennet, the second of five daughters, faces societal pressure to marry well in Regency England. "
            "Her initial prejudice against the proud Mr. Darcy leads to misunderstandings, but both characters grow and change. "
            "Family dynamics, social status, and personal integrity are tested as love triumphs over pride.\n"
            "Jane Austen’s wit and keen social commentary shine through the lively dialogue. "
            "The novel explores the limitations placed on women and the importance of marrying for love. "
            "Elizabeth’s independence and intelligence make her a timeless protagonist."
        ),
        "themes": ["love", "class", "marriage", "prejudice", "family", "society"],
    },
    "The Great Gatsby": {
        "short": "A portrayal of the American Dream and the moral decay of the 1920s. Jay Gatsby’s obsession with wealth and Daisy Buchanan leads to inevitable tragedy.",
        "full": (
            "Nick Carraway narrates his experiences among the wealthy elite of Long Island, focusing on the enigmatic Jay Gatsby. "
            "Gatsby’s lavish parties mask his longing for Daisy Buchanan, a love lost to time and circumstance. "
            "The pursuit of wealth and status ultimately leads to betrayal and death.\n"
            "F. Scott Fitzgerald’s prose captures the glamour and emptiness of the Jazz Age. "
            "The green light at the end of Daisy’s dock symbolizes unattainable dreams. "
            "The novel critiques materialism and the illusion of the American Dream."
        ),
        "themes": [
            "American Dream",
            "wealth",
            "love",
            "illusion",
            "tragedy",
            "society",
        ],
    },
    "Harry Potter and the Sorcerer's Stone": {
        "short": "An orphan discovers he is a wizard and begins his magical education at Hogwarts. Alongside new friends, he uncovers secrets about his parents' past and a dark wizard seeking immortality.",
        "full": (
            "Harry Potter, raised by neglectful relatives, learns on his eleventh birthday that he is a wizard. "
            "At Hogwarts School of Witchcraft and Wizardry, he befriends Ron and Hermione and faces magical challenges. "
            "Harry discovers his connection to the dark wizard Voldemort, who killed his parents.\n"
            "The trio’s bravery and loyalty are tested as they protect the Sorcerer’s Stone. "
            "Themes of friendship, courage, and self-discovery are central to the story. "
            "J.K. Rowling’s world-building introduces readers to a rich magical universe."
        ),
        "themes": ["magic", "friendship", "courage", "identity", "good vs evil"],
    },
    "The Catcher in the Rye": {
        "short": "Holden Caulfield recounts a few days of his life in New York City after being expelled from prep school. The novel explores themes of teenage alienation and existential angst.",
        "full": (
            "Holden Caulfield, disillusioned and cynical, wanders New York City after being expelled from Pencey Prep. "
            "He struggles with the phoniness of the adult world and his own feelings of loss and confusion. "
            "Holden’s narrative voice is raw, honest, and often unreliable.\n"
            "His longing to protect innocence is symbolized by his fantasy of being the 'catcher in the rye.' "
            "The novel explores mental health, grief, and the challenges of growing up. "
            "J.D. Salinger’s work remains a touchstone for adolescent alienation."
        ),
        "themes": [
            "alienation",
            "adolescence",
            "identity",
            "innocence",
            "mental health",
        ],
    },
    "Brave New World": {
        "short": "In a futuristic society driven by technology and instant gratification, individuals are conditioned to conform. Bernard Marx seeks meaning in a world where happiness is manufactured and individuality is suppressed.",
        "full": (
            "Aldous Huxley imagines a future where people are engineered for specific roles and kept docile with pleasure and drugs. "
            "Bernard Marx and Lenina Crowne visit a Savage Reservation, confronting the costs of their society’s stability. "
            "John the Savage, raised outside the system, becomes a tragic figure when brought to London.\n"
            "The novel critiques consumerism, loss of individuality, and the dangers of state control. "
            "Soma, the happiness drug, symbolizes escapism and denial. "
            "Huxley’s vision remains relevant in debates about technology and freedom."
        ),
        "themes": ["dystopia", "technology", "conformity", "freedom", "identity"],
    },
    "Moby Dick": {
        "short": "Captain Ahab obsessively hunts the white whale, Moby Dick, on a doomed voyage. The novel explores themes of obsession, revenge, and humanity's struggle with nature.",
        "full": (
            "Ishmael joins the whaling ship Pequod, captained by the vengeful Ahab. "
            "Ahab’s quest to kill Moby Dick, the white whale that maimed him, drives the crew toward destruction. "
            "The narrative blends adventure, philosophy, and detailed descriptions of whaling life.\n"
            "Melville explores fate, free will, and the limits of human knowledge. "
            "The whale becomes a symbol of nature’s power and mystery. "
            "The novel’s complexity and symbolism have inspired generations of readers."
        ),
        "themes": ["obsession", "revenge", "nature", "fate", "madness"],
    },
    "The Alchemist": {
        "short": "Santiago, a young shepherd, dreams of finding treasure in Egypt. His journey becomes a spiritual quest about fulfilling one’s destiny and listening to the heart.",
        "full": (
            "Santiago leaves his home in Spain to pursue a recurring dream of treasure near the Egyptian pyramids. "
            "Along the way, he meets mentors like Melchizedek and the alchemist, learning about omens and the Soul of the World. "
            "His journey is filled with challenges, self-discovery, and spiritual growth.\n"
            "Coelho’s novel emphasizes the importance of following one’s dreams. "
            "The story blends adventure with philosophical reflection. "
            "Santiago’s transformation inspires readers to seek their own Personal Legend."
        ),
        "themes": ["destiny", "spirituality", "journey", "self-discovery", "dreams"],
    },
    "The Lord of the Rings: The Fellowship of the Ring": {
        "short": "Frodo Baggins inherits a powerful ring and sets out on a perilous journey to destroy it. A fellowship forms to help him navigate threats across Middle-earth.",
        "full": (
            "Frodo Baggins is entrusted with the One Ring, a source of immense evil. "
            "He is joined by a diverse fellowship—hobbits, men, an elf, a dwarf, and a wizard—to journey toward Mount Doom. "
            "The group faces betrayal, temptation, and the growing power of Sauron.\n"
            "Tolkien’s epic explores friendship, sacrifice, and the corrupting influence of power. "
            "The landscapes and cultures of Middle-earth are richly detailed. "
            "The story sets the stage for the larger struggle between good and evil."
        ),
        "themes": ["friendship", "good vs evil", "power", "sacrifice", "adventure"],
    },
    "Jane Eyre": {
        "short": "An orphaned girl becomes a governess and falls in love with her employer, Mr. Rochester. Dark secrets threaten their relationship as she seeks independence and self-respect.",
        "full": (
            "Jane Eyre endures a harsh childhood before finding work at Thornfield Hall. "
            "She falls in love with the brooding Mr. Rochester, only to discover he harbors a tragic secret. "
            "Jane’s moral integrity and desire for autonomy guide her decisions.\n"
            "Charlotte Brontë’s novel blends romance, gothic mystery, and social criticism. "
            "Jane’s resilience and self-worth challenge Victorian gender roles. "
            "The story is celebrated for its emotional depth and strong heroine."
        ),
        "themes": ["independence", "love", "morality", "identity", "gothic"],
    },
    "Frankenstein": {
        "short": "Victor Frankenstein creates a living being from dead tissue, only to be horrified by his creation. The novel raises questions about scientific ethics and human responsibility.",
        "full": (
            "Victor Frankenstein’s obsession with conquering death leads him to create a sentient creature. "
            "Rejected by society and his creator, the creature seeks companionship and revenge. "
            "The narrative alternates between Victor’s and the creature’s perspectives.\n"
            "Mary Shelley’s novel explores the dangers of unchecked ambition. "
            "Themes of isolation, empathy, and the limits of science are central. "
            "The story is a foundational work of both science fiction and gothic literature."
        ),
        "themes": ["science", "creation", "isolation", "responsibility", "ambition"],
    },
    "Crime and Punishment": {
        "short": "Raskolnikov, a poor student in St. Petersburg, believes he's above moral law and commits murder. The psychological drama explores guilt, redemption, and justice.",
        "full": (
            "Raskolnikov murders a pawnbroker, rationalizing his crime as a means to a greater good. "
            "Haunted by guilt and paranoia, he is drawn into a psychological battle with detective Porfiry. "
            "The support of Sonia, a compassionate prostitute, leads him toward confession and redemption.\n"
            "Dostoevsky delves into the complexities of morality and conscience. "
            "The novel examines poverty, alienation, and the search for meaning. "
            "Raskolnikov’s journey is both a crime story and a philosophical exploration."
        ),
        "themes": ["guilt", "redemption", "justice", "morality", "psychology"],
    },
    "Wuthering Heights": {
        "short": "A dark romance between Heathcliff and Catherine Earnshaw spans generations. Set on the moors, the story is full of passion, revenge, and haunting memories.",
        "full": (
            "Heathcliff, an orphan, is adopted by the Earnshaw family and forms a tumultuous bond with Catherine. "
            "Their love is destructive, leading to jealousy, vengeance, and suffering for both families. "
            "The narrative is framed by outsider Mr. Lockwood’s perspective.\n"
            "Emily Brontë’s novel is known for its gothic atmosphere and emotional intensity. "
            "Themes of obsession, social class, and the supernatural pervade the story. "
            "The moorland setting mirrors the characters’ wild passions."
        ),
        "themes": ["love", "revenge", "obsession", "class", "gothic"],
    },
    "Animal Farm": {
        "short": "A group of farm animals overthrow their human owner to create an equal society, only to watch it devolve into a dictatorship. An allegory of the Russian Revolution.",
        "full": (
            "Led by the pigs Napoleon and Snowball, the animals of Manor Farm rebel against Mr. Jones. "
            "Their vision of equality is corrupted as the pigs seize power and become indistinguishable from humans. "
            "The commandments of Animalism are gradually rewritten to justify the new regime.\n"
            "Orwell’s allegory critiques totalitarianism and the betrayal of revolutionary ideals. "
            "The phrase 'All animals are equal, but some animals are more equal than others' encapsulates the novel’s irony. "
            "The story remains a powerful warning about the abuse of power."
        ),
        "themes": ["allegory", "power", "corruption", "revolution", "equality"],
    },
    "Dracula": {
        "short": "Jonathan Harker encounters Count Dracula, a vampire seeking to move from Transylvania to England. A band of friends unite to battle the growing darkness.",
        "full": (
            "Jonathan Harker travels to Transylvania and becomes a prisoner in Dracula’s castle. "
            "Dracula relocates to England, spreading terror and preying on Lucy Westenra. "
            "Professor Van Helsing leads a group to hunt the vampire and save Mina Harker.\n"
            "Bram Stoker’s novel blends horror, romance, and adventure. "
            "Themes of sexuality, superstition, and modernity clash throughout the story. "
            "Dracula’s legacy endures as a defining work of Gothic fiction."
        ),
        "themes": ["vampires", "good vs evil", "supernatural", "fear", "gothic"],
    },
    "The Picture of Dorian Gray": {
        "short": "Dorian Gray remains youthful while his portrait ages, reflecting his moral corruption. A cautionary tale of vanity, indulgence, and consequence.",
        "full": (
            "Dorian Gray, influenced by Lord Henry, wishes to remain forever young while his portrait bears the marks of age and sin. "
            "He pursues pleasure without regard for morality, leading to the ruin of those around him. "
            "The portrait becomes a symbol of his decaying soul.\n"
            "Oscar Wilde’s novel explores aestheticism, duality, and the cost of indulgence. "
            "Dorian’s downfall is both inevitable and tragic. "
            "The story remains a meditation on beauty and consequence."
        ),
        "themes": ["vanity", "morality", "corruption", "aesthetics", "duality"],
    },
    "The Chronicles of Narnia: The Lion, the Witch and the Wardrobe": {
        "short": "Four siblings discover a magical land ruled by a tyrannical witch. They join forces with the lion Aslan to bring peace to Narnia.",
        "full": (
            "Lucy, Edmund, Susan, and Peter stumble through a wardrobe into the magical land of Narnia. "
            "They join the lion Aslan in a battle against the White Witch, who has plunged Narnia into eternal winter. "
            "Edmund’s betrayal and redemption are central to the plot.\n"
            "C.S. Lewis’s story blends fantasy, allegory, and adventure. "
            "Themes of sacrifice, forgiveness, and faith are woven throughout. "
            "The novel is beloved for its imaginative world and moral lessons."
        ),
        "themes": ["fantasy", "good vs evil", "sacrifice", "redemption", "faith"],
    },
    "Fahrenheit 451": {
        "short": "In a future where books are banned, fireman Guy Montag burns them for a living. After meeting a free-thinking girl, he begins to question everything.",
        "full": (
            "Guy Montag’s job is to burn books in a society that fears independent thought. "
            "Encounters with Clarisse, a curious neighbor, and Faber, a former professor, awaken his doubts. "
            "Montag rebels, becoming a fugitive as he seeks meaning in a censored world.\n"
            "Ray Bradbury’s novel warns against censorship and conformity. "
            "The mechanical hound and parlor walls symbolize technological control. "
            "The story champions the enduring power of literature and free thought."
        ),
        "themes": ["censorship", "freedom", "conformity", "technology", "rebellion"],
    },
    "The Hunger Games": {
        "short": "In a dystopian future, Katniss Everdeen volunteers to take her sister's place in a deadly televised competition. She must rely on her instincts and cunning to survive the brutal Hunger Games.",
        "full": (
            "Katniss Everdeen lives in a society where children are forced to fight to the death for entertainment. "
            "She volunteers for the Games to save her sister, forming alliances and outsmarting her opponents. "
            "Her defiance sparks hope and rebellion among the oppressed districts.\n"
            "Suzanne Collins’s novel explores survival, sacrifice, and the effects of violence. "
            "The love triangle with Peeta and Gale adds emotional complexity. "
            "The story critiques reality TV and authoritarian control."
        ),
        "themes": ["dystopia", "survival", "rebellion", "sacrifice", "oppression"],
    },
    "The Giver": {
        "short": "Jonas lives in a seemingly perfect society without pain or choice. When he is chosen to receive memories of the past, he discovers dark truths about his world.",
        "full": (
            "Jonas is selected to be the Receiver of Memory, learning about emotions, color, and history from the Giver. "
            "He realizes his community’s peace comes at the cost of individuality and freedom. "
            "Jonas escapes, hoping to bring change to his world.\n"
            "Lois Lowry’s novel raises questions about conformity, memory, and the value of emotion. "
            "The ambiguous ending invites reflection on hope and resistance. "
            "The story is a classic of young adult dystopian fiction."
        ),
        "themes": ["dystopia", "memory", "freedom", "conformity", "emotion"],
    },
    "Little Women": {
        "short": "The story of the March sisters—Meg, Jo, Beth, and Amy—as they grow up during the Civil War. It explores themes of family, ambition, and womanhood.",
        "full": (
            "The four March sisters navigate adolescence and adulthood, each with distinct dreams and personalities. "
            "Jo’s ambition to become a writer, Meg’s desire for domestic happiness, Beth’s kindness, and Amy’s artistic aspirations shape their journeys. "
            "The family endures hardship, love, and loss together.\n"
            "Louisa May Alcott’s novel celebrates sisterhood and resilience. "
            "The story reflects changing roles for women in the 19th century. "
            "Its warmth and realism have made it a beloved classic."
        ),
        "themes": ["family", "womanhood", "ambition", "sisterhood", "growth"],
    },
    "The Secret Garden": {
        "short": "Mary Lennox discovers a hidden, neglected garden on her uncle’s estate and brings it back to life. The story is one of healing, friendship, and renewal.",
        "full": (
            "Mary Lennox, a lonely and spoiled child, is sent to live with her uncle in Yorkshire. "
            "She discovers a locked garden and, with the help of Dickon and Colin, restores it to beauty. "
            "The process transforms all three children, bringing joy and health.\n"
            "Frances Hodgson Burnett’s novel explores the healing power of nature and friendship. "
            "Themes of loss, hope, and personal growth are central. "
            "The garden becomes a symbol of renewal and possibility."
        ),
        "themes": ["healing", "friendship", "nature", "renewal", "growth"],
    },
    "The Kite Runner": {
        "short": "Amir, a boy from Kabul, reflects on his betrayal of a loyal friend and seeks redemption. A powerful tale of friendship, guilt, and the scars of war.",
        "full": (
            "Amir’s childhood friendship with Hassan is shattered by an act of betrayal. "
            "Years later, Amir returns to Taliban-ruled Afghanistan to atone for his past. "
            "The story spans decades, exploring family, loyalty, and forgiveness.\n"
            "Khaled Hosseini’s novel examines the impact of guilt and the possibility of redemption. "
            "The backdrop of Afghan history adds depth and urgency. "
            "The relationship between fathers and sons is a recurring theme."
        ),
        "themes": ["friendship", "guilt", "redemption", "family", "war"],
    },
    "Life of Pi": {
        "short": "After a shipwreck, young Pi Patel is stranded on a lifeboat with a Bengal tiger. His journey becomes one of survival, faith, and imagination.",
        "full": (
            "Pi Patel survives a shipwreck and shares a lifeboat with a tiger named Richard Parker. "
            "He uses ingenuity and faith to endure months at sea, facing hunger, storms, and fear. "
            "The story blurs the line between reality and imagination.\n"
            "Yann Martel’s novel explores spirituality, storytelling, and the will to survive. "
            "The ambiguous ending invites readers to question truth and belief. "
            "The relationship between Pi and the tiger is both literal and symbolic."
        ),
        "themes": ["survival", "faith", "imagination", "storytelling", "nature"],
    },
    "A Tale of Two Cities": {
        "short": "Set during the French Revolution, the novel contrasts the cities of London and Paris. Themes include sacrifice, justice, and resurrection.",
        "full": (
            "Charles Darnay and Sydney Carton are linked by love for Lucie Manette and the turmoil of revolution. "
            "Carton’s ultimate sacrifice redeems his wasted life and saves Darnay from the guillotine. "
            "The novel’s famous opening and closing lines frame a story of upheaval and hope.\n"
            "Charles Dickens explores themes of fate, justice, and transformation. "
            "The violence of the revolution is contrasted with acts of compassion. "
            "The story’s scope and emotion have made it a classic of historical fiction."
        ),
        "themes": ["revolution", "sacrifice", "justice", "redemption", "history"],
    },
    "Great Expectations": {
        "short": "Pip, a poor orphan, navigates class, ambition, and love after receiving an unexpected fortune. A story of personal growth and moral development.",
        "full": (
            "Pip’s life changes when he receives money from a mysterious benefactor. "
            "He aspires to become a gentleman and win the love of Estella, raised by the bitter Miss Havisham. "
            "Pip’s journey is marked by disappointment, self-discovery, and forgiveness.\n"
            "Dickens’s novel examines social class, ambition, and the meaning of true wealth. "
            "The eccentric characters and vivid settings are hallmarks of his style. "
            "Pip’s growth from naïveté to maturity is central to the story."
        ),
        "themes": ["ambition", "class", "love", "growth", "forgiveness"],
    },
    "Emma": {
        "short": "Emma Woodhouse is a wealthy young woman who fancies herself a matchmaker. Her misguided meddling leads to romantic complications and self-discovery.",
        "full": (
            "Emma Woodhouse enjoys orchestrating the love lives of her friends, often with unintended consequences. "
            "Her friendship with Harriet Smith and rivalry with Jane Fairfax complicate matters. "
            "Emma’s own feelings for Mr. Knightley emerge as she learns humility and empathy.\n"
            "Jane Austen’s wit and social observation are on full display. "
            "The novel explores class, gender, and the pitfalls of pride. "
            "Emma’s journey to self-awareness is both humorous and touching."
        ),
        "themes": ["romance", "society", "pride", "self-discovery", "class"],
    },
    "Don Quixote": {
        "short": "An aging man becomes a self-declared knight and sets out on absurd adventures with his loyal squire. A satirical exploration of idealism and reality.",
        "full": (
            "Alonso Quixano, inspired by chivalric romances, becomes Don Quixote and sets out to revive knighthood. "
            "His delusions lead to comic misadventures, including tilting at windmills. "
            "Sancho Panza, his practical squire, provides a grounding counterpoint.\n"
            "Cervantes’s novel is a rich satire of literature and society. "
            "Themes of illusion, madness, and the power of imagination are central. "
            "The story’s influence on Western literature is profound."
        ),
        "themes": ["satire", "idealism", "reality", "imagination", "madness"],
    },
    "Les Misérables": {
        "short": "Jean Valjean, a former convict, seeks redemption while being pursued by Inspector Javert. The story spans revolution, love, and justice in 19th-century France.",
        "full": (
            "Jean Valjean’s transformation from prisoner to benefactor is at the heart of the novel. "
            "He adopts Cosette, evades the relentless Javert, and becomes involved in the Paris uprising. "
            "The lives of many characters intersect in a sweeping tale of suffering and hope.\n"
            "Victor Hugo explores justice, mercy, and the struggle for dignity. "
            "The novel’s scope encompasses poverty, politics, and love. "
            "Its emotional power and social critique remain relevant."
        ),
        "themes": ["redemption", "justice", "love", "revolution", "mercy"],
    },
    "The Count of Monte Cristo": {
        "short": "Wrongfully imprisoned, Edmond Dantès escapes and plots his revenge. A tale of betrayal, transformation, and retribution.",
        "full": (
            "Edmond Dantès is betrayed by friends and imprisoned in Château d’If. "
            "He escapes, discovers a hidden treasure, and reinvents himself as the Count of Monte Cristo. "
            "Dantès meticulously enacts revenge on those who wronged him.\n"
            "Alexandre Dumas’s novel explores justice, vengeance, and forgiveness. "
            "Themes of fate, identity, and transformation are central. "
            "The story’s intrigue and adventure have captivated readers for generations."
        ),
        "themes": ["revenge", "justice", "betrayal", "transformation", "forgiveness"],
    },
    "The Odyssey": {
        "short": "Homer’s epic poem follows Odysseus as he journeys home from the Trojan War, facing mythical creatures and divine wrath.",
        "full": (
            "Odysseus’s voyage home to Ithaca is fraught with peril, including encounters with the Cyclops, Sirens, and Scylla and Charybdis. "
            "He relies on cunning and resilience to overcome obstacles set by gods and monsters. "
            "His wife Penelope and son Telemachus await his return, fending off suitors.\n"
            "The epic explores themes of heroism, loyalty, and perseverance. "
            "Homer’s storytelling blends adventure, myth, and moral lessons. "
            "Odysseus’s journey is a foundational narrative of Western literature."
        ),
        "themes": ["adventure", "heroism", "perseverance", "myth", "loyalty"],
    },
    "Beowulf": {
        "short": "An ancient hero fights monsters and dragons to protect his people. Themes of bravery, loyalty, and legacy dominate this Old English epic.",
        "full": (
            "Beowulf travels to Denmark to defeat the monster Grendel, then battles Grendel’s vengeful mother. "
            "Years later, as king, he faces a deadly dragon threatening his people. "
            "Beowulf’s courage and sacrifice secure his legacy.\n"
            "The poem explores the values of honor, loyalty, and heroism. "
            "Its language and structure reflect the oral tradition. "
            "Beowulf’s story endures as a symbol of the heroic ideal."
        ),
        "themes": ["heroism", "bravery", "loyalty", "legacy", "sacrifice"],
    },
    "Dr. Jekyll and Mr. Hyde": {
        "short": "Dr. Jekyll’s experiments unleash his violent alter ego, Mr. Hyde. A psychological thriller about duality and the nature of evil.",
        "full": (
            "Dr. Henry Jekyll creates a potion to separate his good and evil sides. "
            "His alter ego, Mr. Hyde, commits increasingly violent acts. "
            "Jekyll’s struggle to control Hyde leads to tragedy and self-destruction.\n"
            "Robert Louis Stevenson’s novella explores the duality of human nature. "
            "Themes of repression, morality, and identity are central. "
            "The story’s suspense and symbolism have made it a classic."
        ),
        "themes": ["duality", "evil", "identity", "repression", "psychology"],
    },
    "Treasure Island": {
        "short": "Young Jim Hawkins sets off on a sea voyage in search of pirate treasure. The classic adventure explores greed, courage, and betrayal.",
        "full": (
            "Jim Hawkins discovers a treasure map and joins a voyage led by the enigmatic Long John Silver. "
            "Mutiny, danger, and shifting loyalties test Jim’s bravery and judgment. "
            "The search for treasure leads to both peril and self-discovery.\n"
            "Robert Louis Stevenson’s novel is a defining work of adventure fiction. "
            "Themes of greed, trust, and coming of age are central. "
            "The story’s pirates and settings have become cultural icons."
        ),
        "themes": ["adventure", "greed", "courage", "betrayal", "coming of age"],
    },
    "The Adventures of Huckleberry Finn": {
        "short": "Huck Finn escapes an abusive father and travels down the Mississippi River with a runaway slave. A critique of racism and society in pre-Civil War America.",
        "full": (
            "Huck fakes his own death to escape his father and teams up with Jim, a runaway slave. "
            "Their journey down the river exposes the hypocrisy and cruelty of society. "
            "Huck’s moral dilemmas challenge the values he’s been taught.\n"
            "Mark Twain’s novel is celebrated for its humor, realism, and social critique. "
            "Themes of freedom, friendship, and conscience are central. "
            "The story’s language and perspective are uniquely American."
        ),
        "themes": ["freedom", "racism", "friendship", "society", "conscience"],
    },
    "The Time Machine": {
        "short": "A scientist travels far into the future and discovers the fate of humanity. H.G. Wells explores class division, progress, and decay.",
        "full": (
            "The Time Traveller journeys to the distant future, encountering the gentle Eloi and the subterranean Morlocks. "
            "He discovers a world shaped by class division and evolutionary change. "
            "His adventures raise questions about progress and the fate of civilization.\n"
            "H.G. Wells’s novel is a cornerstone of science fiction. "
            "Themes of time, technology, and social critique are central. "
            "The story’s imagination and insight remain influential."
        ),
        "themes": ["time travel", "class", "progress", "decay", "science fiction"],
    },
    "Around the World in 80 Days": {
        "short": "Phileas Fogg wagers he can circumnavigate the globe in 80 days. A fast-paced adventure full of unexpected challenges and encounters.",
        "full": (
            "Phileas Fogg, a precise Englishman, bets his fortune on traveling around the world in 80 days. "
            "Accompanied by his loyal servant Passepartout, he faces delays, rescues, and pursuit by Detective Fix. "
            "The journey tests Fogg’s resolve and adaptability.\n"
            "Jules Verne’s novel celebrates curiosity, ingenuity, and perseverance. "
            "The story’s pace and variety of settings keep readers engaged. "
            "Fogg’s transformation is as important as the outcome of his wager."
        ),
        "themes": ["adventure", "travel", "perseverance", "ingenuity", "challenge"],
    },
    "Anne of Green Gables": {
        "short": "Anne Shirley, a spirited orphan, is adopted by siblings on Prince Edward Island. Her imagination and curiosity bring joy and chaos to their quiet lives.",
        "full": (
            "Anne Shirley’s vivid imagination and fiery temper make her both endearing and troublesome. "
            "She forms deep friendships, excels in school, and gradually wins the hearts of Marilla and Matthew Cuthbert. "
            "Anne’s adventures are filled with humor, mishaps, and growth.\n"
            "L.M. Montgomery’s novel celebrates individuality, optimism, and the beauty of nature. "
            "Themes of belonging, forgiveness, and self-acceptance are central. "
            "Anne’s journey from outsider to beloved community member is inspiring."
        ),
        "themes": ["imagination", "belonging", "growth", "friendship", "nature"],
    },
}

with open(txt_out, "w", encoding="utf-8") as f_txt:
    for title, data in book_summaries_dict.items():
        short = data["short"].strip()
        themes_str = "; ".join(data.get("themes", []))
        f_txt.write(f"## Title: {title}::{short}||themes: {themes_str}\n")


with open(dict_out, "w", encoding="utf-8") as f_json:
    json.dump(book_summaries_dict, f_json, indent=2, ensure_ascii=False)

print("TXT saved at:", txt_out.resolve())
print("JSON saved at:", dict_out.resolve())
