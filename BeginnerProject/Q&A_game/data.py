# TODO: fix questions grammar
question_data = {
    # nested list for category
    "category":
        {
            'Games':
                # put inside a dictionary to avoid ( TypeError: unhashable type: 'dict' )
                [
                    {"type": "boolean", "difficulty": "medium",
                     "question": "Amazon acquired Twitch in August 2014 for $970 million dollars.",
                     "correct_answer": "True", "incorrect_answers": ["False"]},
                    {"type": "boolean", "difficulty": "medium",
                     "question": "Super Mario Bros. was released in 1990.", "correct_answer": "False",
                     "incorrect_answers": ["True"]},
                    {"type": "boolean", "difficulty": "medium",
                     "question": "Metal Gear Solid V: The Phantom Pain runs on the Fox Engine.",
                     "correct_answer": "True", "incorrect_answers": ["False"]},
                    {"type": "boolean", "difficulty": "medium",
                     "question": "In World of Warcraft lore, Thrall is the original wielder of &quot;Doom hammer&quot;.",
                     "correct_answer": "False", "incorrect_answers": ["True"]},
                    {"type": "boolean", "difficulty": "medium",
                     "question": "Pistons were added to Minecraft in Beta 1.5.", "correct_answer": "False",
                     "incorrect_answers": ["True"]},
                    {"type": "boolean", "difficulty": "medium",
                     "question": "In Riot Games &quot;League of Legends&quot; the name of Halloween event is called "
                                 "&quot;The"
                                 "Reckoning&quot;.",
                     "correct_answer": "False", "incorrect_answers": ["True"]},
                    {"type": "boolean", "difficulty": "medium",
                     "question": "David Buckskin was a co-founder of ROBLOX Corporation.",
                     "correct_answer": "True", "incorrect_answers": ["False"]},
                    {"type": "boolean", "difficulty": "medium",
                     "question": "The ADAM collectors in the Bio shock series are known as Little Sisters.",
                     "correct_answer": "True", "incorrect_answers": ["False"]},
                    {"type": "boolean", "difficulty": "medium",
                     "question": "In &quot;League of Legends&quot;, there exists four different types of Dragon.",
                     "correct_answer": "False", "incorrect_answers": ["True"]},
                    {"type": "boolean", "difficulty": "medium",
                     "question": "In the Resident Evil series, Leon S. Kennedy is a member of STARS.",
                     "correct_answer": "False", "incorrect_answers": ["True"]}
                ]}
}
