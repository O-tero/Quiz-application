import random
from string import ascii_lowercase

NUM_QUESTIONS_PER_QUIZ = 5
QUESTIONS = {
    "Which team has won most NBA conference championships?": [
        "Miami Heat",
        "Los Angeles Lakers",
        "Boston Celtics",
        "Denver Nuggets",
    ],
    "Who holds the record for the most points scored over their career?": [
        "Kareem Abdul-Jabbar",
        "Karl Malone",
        "LeBron James",
        "Michael Jordan",
    ],
    "Which player was drafted #1 at the 2003 NBA Draft?": [
        "Chris Bosh",
        "Darko Milicic",
        "LeBron James",
        "Dwyane Wade",
    ],
    "Which of these franchises never relocated?": [
        "Toronto Raptors",
        "Memphis Grizzlies",
        "Atlanta Hawks",
        "Los Angeles Clippers",
    ],
    "Who holds the record for most rebounds in one season?": [
        "Bill Russell",
        "Ben Wallace",
        "Shaquille O'Neal",
        "Wilt Chamberlain",
    ],
    "Which player was Magic Johnson's teammate on the Lakers?": [
        "A.C. Green",
        "Jerry West",
        "Kobe Bryant",
        "Robert Parish",
    ],
    "During which decade was the 24-second shot clock introduced in the NBA?": [
        "1950s",
        "1960s",
        "1970s",
        "1980s",
    ],
    "Which player has won four MVPs in five years?": [
        "Michael Jordan",
        "Larry Bird",
        "Wilt Chamberlain",
        "Bill Russell",
    ],
    "Which player has never won a Defensive Player of the Year Award?": [
        "Tim Duncan",
        "Kevin Garnett",
        "Dennis Rodman",
        "Michael Jordan",
    ],
    "Which player played his entire career with the same franchise?": [
        "Michael Jordan",
        "Reggie Miller",
        "Karl Malone",
        "Tim Duncan",
    ],
    "Which city hosted the first NBA All-Star Game, back in 1951?": [
        "New York",
        "Boston",
        "St. Louis",
        "Los Angeles",
    ],
    "Who holds the record for most career steals in the NBA?": [
        "John Stockton",
        "Jason Kidd",
        "Gary Payton",
        "Scottie Pippen",
    ],
    "Which of these coaches has the highest career winning percentage?": [
        "Red Auerbach",
        "Phil Jackson",
        "Pat Riley",
        "Chuck Daly",
    ],
}

