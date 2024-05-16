QUESTIONS = {
    "Which team has won most NBA conference championships?"[
        "A.Miami Heat" "B. Los Angeles Lakers" "C. Boston Celtics" "D. Denver Nuggets"
    ],
    "Who holds the record for the most points scored over their career?"[
        "A. Kareem Abdul-Jabbar" "B. Karl Malone" "C. LeBron James" "D. Michael Jordan"
    ],
    "Which player was drafted #1 at the 2003 NBA Draft?"[
        "A. Chris Bosh" "B. Darko Milicic" "C. LeBron James" "D. Dwyane Wade"
    ],
    "Which of these franchises never relocated?"[
        "A. Toronto Raptors"
        "B. Memphis Grizzlies"
        "C. Atlanta Hawks"
        "D. Los Angeles Clippers"
    ],
    "Who holds the record for most rebounds in one season?"[
        "A. Bill Russell" "B. Ben Wallace" "C. Shaquille O'Neal" "D. Wilt Chamberlain"
    ],
    "Which player was Magic Johnson's teammate on the Lakers?"[
        "A. A.C. Green" "B. Jerry West" "C. Kobe Bryant" "D. Robert Parish"
    ],
    "During which decade was the 24-second shot clock introduced in the NBA?"[
        "A. 1950s" "B. 1960s" "C. 1970s" "D. 1980s"
    ],
    "Which player has won four MVPs in five years?"[
        "A. Michael Jordan" "B. Larry Bird" "C. Wilt Chamberlain" "D. Bill Russell"
    ],
    "Which player has never won a Defensive Player of the Year Award?"[
        "A. Tim Duncan" "B. Kevin Garnett" "C. Dennis Rodman" "D. Michael Jordan"
    ],
    "Which player played his entire career with the same franchise?"[
        "A. Michael Jordan" "B. Reggie Miller" "C. Karl Malone" "D. Tim Duncan"
    ],
    "Which city hosted the first NBA All-Star Game, back in 1951?"[
        "A. New York" "B. Boston" "C. St. Louis" "D. Los Angeles"
    ],
    "Who holds the record for most career steals in the NBA?"[
        "A. John Stockton" "B. Jason Kidd" "C. Gary Payton" "D. Scottie Pippen"
    ],
    "Which of these coaches has the highest career winning percentage?"[
        "A. Red Auerbach" "B. Phil Jackson" "C. Pat Riley" "D. Chuck Daly"
    ],
}
for question, alternatives in QUESTIONS.items():
    correct_answer = alternatives[0]
    sorted_alternatives = sorted(alternatives)
    for label, alternative in enumerate(sorted_alternatives):
         print(f"  {label}) {alternative}")
         
    answer_label = int(input(f"{question}? "))
    answer = sorted_alternatives[answer_label]
    if answer == correct_answer:
        print("Correct!")
    else:
        print(f"The answer is {correct_answer!r}, not {answer!r}")
