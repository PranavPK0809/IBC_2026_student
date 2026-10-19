days = ["First", "Second", "Third", "Fourth", "Fifth", "Sixth",
        "Seventh", "Eigth", "Ninth", "Tenth", "Eleventh", "Twelfth"]

gifts = ["A Partridge in a Pear Tree",
         "Two Turtle Doves, and",
         "Three French Hens",
         "Four Colly Birds",
         "Five Gold Rings",
         "Six Geese-a-Laying",
         "Seven Swans-a-Swimming",
         "Eight Maids-a-Milking",
         "Nine Ldaies Dancing",
         "Ten Lords-a-Leaping",
         "Eleven Pipers Piping",
         "Twelve Drummers Drumming"]

for i in range(0,12):
    print("On the", days[i], "day of Christmas my true love gave to me:")

    for j in range(i,-1,-1):
        print(gifts[j])

    print()