---
title: "Notes on my FOSDEM 2026 Talk: My Grandma Needed a New Computer?"
date: "2026-02-14"
categories: [events, talks]
image: "thumbnail.jpg"
other-links:
  - text: Comment on GitHub
    icon: chat
    href: https://github.com/rnd195/rnd195.github.io-comments/issues/6
    target: _blank

---


Providing an extended view on my short talk at FOSDEM 2026 

![Image from [FOSDEM.org](https://fosdem.org/2026/schedule/event/G3ZWYU-lightning_lightning_talks_2/) under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/deed.en)](thumbnail.jpg){fig-alt="A screenshot of a recording of a presentation"}

---

Earlier this month, I had the great privilege of speaking at the FOSDEM 2026 conference in the "lightning *lightning* talk" section. In this segment, presenters speak about seemingly random topics generally centered around free and open source technologies with 256 seconds to get the point across.

In my talk titled "My Grandma Needed a New Computer?", I told a personal story about a project I undertook with my grandma and her PC. The main issue was that her computer was running Windows 10, which was due to reach the end of support. Additionally, because of old hardware, there was no long-term sustainable way to upgrade her system to the next version. You can probably guess where this is going, but in this post, I would like to go over some of my slides and what I said during the talk with the goal of providing more information and nuance about the seemingly silly story.

::: {.callout-tip}
- Here is a link to the recording of my presentation: [Video with timestamp](https://mirror.cyberbits.eu/fosdem/2026/janson/G3ZWYU-lightning_lightning_talks_2.av1.webm#t=2093)
- Alternatively, here's a link to the [Lightning lightning talks 2 session](https://fosdem.org/2026/schedule/event/G3ZWYU-lightning_lightning_talks_2/) page with the recording at the bottom of the page (my segment starts at around 34:55)

:::

# Notes on Some Slides

::: {.callout-note collapse="true"}

## Slide 3/12 (click to show)

![](index.assets/0003 (Small).jpg)

:::

> *Those of you that manage a device for some of your family members, I'm guessing you had to deal with the end of support of Windows 10 back in October. Those of you that didn't, the problem was that in order to officially upgrade, your device needed to have some minimum hardware requirements. So doing nothing meant that you would receive no security updates, for example. And there were some estimates that up to 400 million devices were affected, but who really knows? What I do know is that my grandma's computer was one of these devices, and because I manage it for her, it was also my problem.* 

At this point in time, it appears that some devices with unsupported hardware can be upgraded, according to ZDNET,[^zd] for example. However, as the contributors of the open source Windows 11 installation utility FlyOOBE[^flyoobe] state: "Works today — but unsupported means you accept the risk". Naturally, Microsoft themselves do not recommend[^ms1] installing the system on an unsupported device, further stating that "these devices aren't guaranteed to receive updates".

Secondly, Microsoft ended up releasing the Extended Security Updates scheme, which lets some users, who have logged into the system with a Microsoft account, receive updates for an extra year.[^esu]

All in all, if you're managing a device for someone, I feel like it is best to take the safest bets in terms of maintenance and compatibility, especially in the long term. I certainly don't want my grandma calling me about seemingly scary-sounding messages popping up on her device about incompatibility and security updates.



::: {.callout-note collapse="true"}

## Slides 4/12 and 5/12

![](index.assets/0004 (Small).jpg)

![](index.assets/0005 (Small).jpg)

:::

> *To give you some context about my grandma and her relationship with tech, let me actually start from the opposite direction, and let's look at some population statistics. So this is a small section from a 2023 survey about Czech households and their relationship with tech, and for us, the important part is that households with people over 65 and no children – only about a half of those even owned a computer, right. If we go further and look at reported skills, then in my grandma's age bracket, only about 23% of people knew how to copy files, and about 6% knew how to install a program.*

I later found out that there exists a 2025 edition[^csu] of the survey in question. In this latest report, the ownership of computers in households with people over 65 and no children actually went down to 49.9%. On the other hand, 25.3% of people between 65 and 74 reported being able to copy files, while 7% said they knew how to install a program. Overall, I believe that these revised numbers don't change what I was trying to illustrate—a large portion of people in my grandma's age bracket aren't well-versed in using a computer, providing a reference point for the audience about what my grandma's capabilities could look like.

What I found very troubling, however, and this is something I haven't touched on in my presentation, is that 38% of people between 65 and 74 have "seen unreliable information" on social media or on news sites, but only 9% (of the total number of people in the age group) checked whether this information was true. And I suppose that this is something many people with older parents or grandparents can relate to: my grandma receives numerous emails and WhatsApp messages from her friends that forward them to her because they received them from other friends, and so on. Unfortunately, I can't really help her with that. I can tell her not to jump to conclusions and apply a healthy dose of skepticism, especially to sensational-sounding information. But even in the best-case scenario where my grandma discards such information immediately after reading it, I feel like it still leaves an imprint in her mind, slowly chiseling at her capability to differentiate between what's fake and what's real. I don't want that. Nobody does.

::: {.callout-note collapse="true"}

## Slide 6/12

![](index.assets/0006 (Small).jpg)

:::

> *So, knowing all this, you would be right to assume that my grandma is not a technical person, but let me just say: that's okay. I mean we all have different hobbies, right... But, unlike a large proportion of her peers, she can copy files, okay? Back in the day, she also was able to install Windows 10, with just me on the phone. But now, all she really uses is a browser, an office suite, and a printer.*

This section contains one of the moments I'm most proud of in my grandma's journey with her computer. More than half a decade ago, Windows 7 was reaching its end of support, and you could upgrade to Windows 10 through a fairly simple process. Regardless of its simplicity, this was something completely unknown to my grandma—the concept of downloading an update to a newer version of her system from the internet, clicking through an installation wizard, and ending up with a different-looking desktop than a few hours ago. I mean, sure, it was 2019-2020 at that time and this must have been fairly standard at that point. But for someone who just reads emails, news, and searches for recipes online, it simply wasn't something my grandma was used to. Regardless, the gist of the story is that she upgraded to Windows 10 with just me on the phone: no screen sharing, no video call, just pure audio waves and an iterative process of finding the right button to press.

::: {.callout-note collapse="true"}

## Slide 9/12

![](index.assets/0009 (Small).jpg)

:::

>And so what can we do about this? I mean, buy her a new computer? Well, I don't know, but there is an obvious solution, right? I mean, here we are. Just install Linux.
>
>So that's what I did.

What a surprising turn of events, right? :)



::: {.callout-note collapse="true"}

## Slide 10/12

![](index.assets/0010 (Small).jpg)

:::

> *Specifically, her computer's running ZorinOS, no affiliation by the way. The reason I chose this distribution was because its desktop environment seemed familiar, or I thought it would be to her. It also works out of the box, seems difficult to mess up, and it's also super simple to run updates through the software updater utility.*

The monitor, keyboard, and mouse pictured in the slide are part of the actual workstation my grandma uses. Fun fact: the keyboard has a PS/2 connector, and it's still working fine. 

One section I ended up cutting due to time constraints was a mention of the OpenPrinting project,[^openprinting] which coincidentally had a booth in this year's conference. To express my gratitude, I briefly thanked the person running the booth, telling them that my grandma's printer works thanks to their efforts, to which they responded with an enthusiastic "let's go!" Thanks again, OpenPrinting contributors!

Regarding software updates, I think it's much more approachable for someone like my grandmother to click on an icon to run updates rather than opening a terminal window and typing something in. I don't think that my grandma was used to installing newer versions of software on her previous system, so this is actually a step up security-wise for her.

::: {.callout-note collapse="true"}

## Slide 11/12

![](index.assets/0011 (Small).jpg)

:::

> *And it's been about six months, there haven't really been any major issues so far. My grandma was even able to print something, completely on her own, without me showing her how, and I thought, honestly, I thought that was pretty impressive and a great testament to the UI of the whole system.*
>
> *But I know that this whole example is not really serious, and it's not something you would draw conclusions from. But regardless, you know, it gave me tremendous hope about the state of Linux desktop, especially for people like my grandma.*
>
> *So to wrap this up, it turns out that my grandma did not meet a new computer, and if you're wondering whether some of your less technical family members would be able to use Linux, just know that my grandma is doing fine. Thank you.*

While there haven't been any major issues, there were some hiccups. For instance, my grandma was somehow able to sign out and get into the login flow where not only was her password required to unlock the device, but she also needed to type in her username. It was a confusing phone call, but it hasn't happened since. 

Regarding the printing story, like many things mentioned in this presentation or post, this may seem trivial to an average tech person. But it's important to keep in mind that, despite the familiar desktop environment of ZorinOS, this was a completely new experience for my grandmother, and it wasn't easy to predict how well she'd interact with the system. It's also worth noting that your browser, PDF viewer, and LibreOffice—all of these have slightly different flows to print a document. What I mean is that one of these can have a dedicated icon with a printer, while the other may require you to navigate to File > Print. Additionally, you're not guaranteed that the window that will pop up once you click either of these options will be the same. Regardless, my grandma was apparently able to navigate through all this and successfully print a document.

::: {.callout-note collapse="true"}

## References Slide

Included for completeness

![](index.assets/0012 (Small).jpg)

:::

## Conclusion

This was supposed to be a lighthearted presentation, and I hope it came across as such. I also saw this as an opportunity to challenge myself to speak in front of a large crowd of people after a while, and I am extremely grateful for it.

Let me close this post by saying that FOSDEM is an impressive feat of human collaboration. As a conference-goer, you have the opportunity to meet so many incredibly talented developers, inspiring individuals, and top-of-the-field people—all of that for free and with an incredible level of coordination. All I can say is: thank you and see you next year.



[^zd]: <https://www.zdnet.com/article/how-to-upgrade-your-incompatible-windows-10-pc-to-windows-11/>
[^flyoobe]: <https://github.com/builtbybel/FlyOOBE?tab=readme-ov-file#-faq>
[^ms1]: <https://support.microsoft.com/en-us/windows/windows-11-on-devices-that-don-t-meet-minimum-system-requirements-0b2dc4a2-5933-4ad4-9c09-ef0a331518f1>
[^esu]: <https://www.microsoft.com/en-us/windows/extended-security-updates>
[^csu]: Czech Statistical Office, 2025. Využívání informačních a komunikačních technologií v domácnostech a mezi osobami. URL: <https://csu.gov.cz/produkty/vyuzivani-informacnich-a-komunikacnich-technologii-v-domacnostech-a-mezi-osobami-gnzqheaxdo>. Subject to [License Terms](https://csu.gov.cz/podminky_pro_vyuzivani_a_dalsi_zverejnovani_statistickych_udaju_csu).

[^openprinting]: <https://openprinting.github.io/>





<br/> [Comment on GitHub](https://github.com/rnd195/rnd195.github.io-comments/issues/6){.btn .btn-secondary title="Comment on GitHub" .bi-chat target="_blank"}
