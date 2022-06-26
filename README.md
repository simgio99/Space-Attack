# Space-Attack
The goal of the challenge is to **decode**, on five different levels of difficulty, cipher text messages that were given to us by *Defence Tech*. All the encoded messages share some similarities, like the common AES encoded substrings at the start and at the end.


# Shared AES parts and first two levels

At the beginning of the challenge, we dove into understanding what was the meaning behind the shared parts accross all the messages. As the given resources mentioned, we successfully identified the *recurring portions* of string within the five messages. The decoding of those portions was done through an AES decoder, using select mode ECB (ElectronicCodeBook),Key Size in 128 Bits and Base64 as output.
The process allowed us to decode the following strings:
<br /> <br />
JaAbDk1QlerxhNo8pLqS2Q== corresponds to *"Start"*
<br />
nij8GNMQUx06N++TLehaxw== corresponds to *"Stop"*

Of course, this evidence implies that the **core** of the messages is contained between the two sequences. 

The first level was pretty straightforward for us, since every member of the team had previously encountered *Base64*, and we were easily able to recognize it by just looking at the string. Through an online tool for the translation of Base64, we were able to translate the string:
<br />

d2VsY29tZSBldmVyeW9uZSB0byBjeWJlciwgdGhpcyBpcyB0aGUgZmlyc3Qgc3RlcCB0byBsZWFkIHlvdXIgdGVhbSB0byB3aW4
<br /> into: <br />
*“welcome everyone to cyber, this is the first step to lead your team to win”*
<br />


The second level went through very smoothly too. A quick glance at the core cipher text gave us the hint that the message was encoded by inverting the initial string.
We wrote a simple python script that allows us to reverse strings, since the same trick might be useful for the next levels, in case they contain multiple encoding layers.
The actual message is a famous line of dialogue exchange during the famous Apollo 13 mission:
<br />
*"tlovrednu suB B niam a dah ev'ew,melborp a dah ev'ew"*
<br />
Which translates to:
<br />
*"we’ve had a problem, we’ve had a main B Bus undervolt"*
<br />



# Third level struggles
The third level is the one for which we spent most of our time.
By looking at the core string, we observed some letters were much more frequent than others.
This gave us the hint to execute an occurrence analysis of the letters of cipher text. To accomplish it, we wrote a python script capable of returning us the sorted number of occurrences for each letter of the string, and this is the results for the level 3 cipher text:
<br /><br />
`['T', 'C', '2', '6', '!', 'B', ' ', '0', 'x', '5', '9', 'D', 'z', 'H', '8', 'q', 'A', 'G', 'J', 'S', ‘W’]`
<br /><br />
Reflecting on the fact that the cardinality of the set of the used characters is 21, and considering that the English alphabet has 26 different letters, we immediately thought that the adopted encoding technique might be a substitution cipher. What initially misled us was the belief that the letter ’T’, which is the most frequent one, was the equivalent substitute of one of the twi most frequently used letters of the alphabet (e or t, proved by the fact that they have the two shortest representations in the morse code). By analyzing the letters near to the T's, we realized that it behaved much like a whitespace. From this point on, the process of building the translation dictionary was quite straightforward, coming up with the following:

`   ['T' : ' ',
    '2' : 'e', 
    'C' : 't', 
    '6' : 'i', 
    'D' : 'u', 
    '!' : 'o', 
    'B' : 's', 
    ' ' : 'n', 
    '0' : 'm', 
    'x' : 'a', 
    '5' : 'h',
    'A' : 'r',
    'z' : 'c',
    'H' : 'y',
    '9' : 'l',
    'W' : ',',
    'q' : 't', 
    'G' : 'x', 
    '8' : 'k', 
    'J' : '1', 
    'S' : '0']
`

We wrote a python script to implement the dictionary substitution, obtaining the following deciphered text: <br />
*“the solution is to use an isl to communicate telemetry to the main station, the next key is 10”* <br />

A possible counter-measure to avoid these kind of “attacks” is to not just apply a substitution cipher right out of the box on the plain text. As other coding systems like the morse code show, an encoding algorithm that maps a letter always with the same letter is vulnerable to frequency analysis and brute-force attacks. A better solution could involve encoding the starting string in base64, and only then apply a substitution cipher to it. This makes it very hard for the attacker to build its own translation dictionary, because the translation process is not going to give any kind of message that resembles natural language anyway.


# The first key 
The clue for the fourth level was the numerical key “10”, so we immediately framed the problem as a numeric deciphering problem. The first solution that we tried was a trivial shift algorithm, trying to achieve the decoding by shifting on the ASCII table by ten (forward or backward). The received output was not resembling any kind of natural language, so we moved on to a “skip-n” algorithm, meaning that after character in the string is picked, the next one in the sequence must be picked after skipping n tokens in the string.
The result had the features of natural language phrasing, but there were some issues in the deciphered text. After some time brainstorming the problem, we found out that there were some issues regarding the “double whitespaces” in the ciphered string, that were incorrectly trimmed off by the copy-paste action. After fixing the issue and reapplying the skip-n decoding algorithm, our team succeeded in finding the correct message:
<br />
*“The priority is to download all the images of Naples that contain ships. The last key AES is password12345678”*
<br />
Also in this case, applying the *skip-n* algorithm directly to plain natural language text gives away a lot of information crucial for the attacker. Even if the key was unknown, the attack could be easily brute-forced by applying shift or skip-n algorithm with random keys and choosing the one with the most plausible output as return.

# End of the challenge
Finally, for the fifth level, as the resources suggest, we simply applied an AES decryption algorithm with the key “password12345678” and the final decrypted message is: <br /> <br />
*“Congratulations! This is the last level of encryption”*
<br /><br />
Every decrypted message, as stated at the beginning of the document, will have the Start and Stop marks at its beginning and end.

