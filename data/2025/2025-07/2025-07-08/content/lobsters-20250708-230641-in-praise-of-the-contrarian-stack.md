---
title: In Praise of the Contrarian Stack
url: https://hackers.pub/@hongminhee/2025/contrarian-stack/en
site_name: lobsters
fetched_at: '2025-07-08T23:06:41.229873'
original_url: https://hackers.pub/@hongminhee/2025/contrarian-stack/en
date: '2025-07-08'
published_date: '2025-07-06T06:22:24.158Z'
description: The author discusses their preference for choosing unconventional or "underdog" tech stacks, which they playfully term "**contrarian stacks**," as opposed to mainstream or "orthodox stacks." They share past experiences such as using Sinatra over Rails, MooTools over Prototype, and Solid over React. While contrarian stacks may present challenges like limited community support and the need for more self-troubleshooting, they also offer opportunities for deeper understanding and potential contributions to open-source projects. These stacks often emerge as reactions to perceived shortcomings in mainstream technologies, leading to innovative designs. Although assembling a contrarian stack can be complex, it provides valuable insights into the underlying technologies. The author argues that while mainstream stacks may be favored by current <abbr title="large language model">LLM</abbr> trends, the learning opportunities from contrarian stacks remain invaluable, encouraging readers
  to explore less-traveled paths for unique insights and growth.
tags: programming
---

# In Praise of the Contrarian Stack

洪 民憙 (Hong Minhee)@hongminhee@hackers.pub

7/6/2025, 6:22:24 AM


I've always had a habit of choosing contrarian technologies when deciding on a tech stack. In the late 2000s, when developing web applications with Ruby, I usedSinatrawithDataMapperinstead ofRails. When using JavaScript frameworks, I opted forMooToolsinstead ofPrototype. In the early 2010s, when developing web applications with Python, I avoidedDjangoand instead usedWerkzeugwithSQLAlchemy. These days, I useSolidandSolidStartinstead ofReactandNext.js. I've come to call this tendency to deliberately avoid mainstream technologies in favor of alternative ones aContrarian Stack. The opposite would probably be something like theConventional Stack.

The most notable characteristic of a Contrarian Stack is that relatively fewer people use it. This means you're likely to encounter more problems, and when troubleshooting, you often can't rely on solutions others have already found—you have to solve issues yourself. However, this becomes an opportunity to develop a deeper understanding of the technology and the field beyond it. For instance, Werkzeug's low level of abstraction meant I essentially had to build an in-house web framework on top of it. Some might consider this "reinventing the wheel," but such "wheel reinvention" has genuinely helped me grow. When Stack Overflow didn't have answers, I had to read the source code directly, which led me to understand the intricate details of the HTTP protocol. And if the technology is open source, you get many more opportunities to contribute to it. The thrill of having your pull request merged is something hard to experience with a Conventional Stack.

Another characteristic of Contrarian Stacks is that they're often latecomers. They're frequently created by people who couldn't tolerate the frustrations of Conventional Stacks. This leads to alternative designs. For example, Solid implementedfine-grained reactivityto avoid React's virtual DOM overhead. And while it's not always the case, these alternative designs are often better than those of Conventional Stacks because they learn from and avoid the mistakes of their predecessors. This gives users of Contrarian Stacks more opportunities to develop a better, more refined understanding of the field compared to those using Conventional Stacks.

Meanwhile, Conventional Stacks often take the form of all-in-one packages. Think of Rails' "convention over configuration," Django's "batteries included," or Next.js's full-stack solution—they're well-integrated to the point where users don't feel the boundaries between the various technologies they encompass. In contrast, Contrarian Stacks often require users to select and assemble various components themselves. While this process is time-consuming, it offers the advantage of choosing the best components for each part, and the assembly process provides an opportunity to gain a deeper understanding of each technology.

This assembly process can sometimes be arduous. The time spent configuring and connecting Sinatra + DataMapper +Haml+Sass, setting up middleware, and debugging errors. But through this process, I gained a deeper understanding of how web frameworks actually work and how each layer connects. And that understanding has been a valuable asset regardless of which stack I've used later.

However, it's important to remember that today's Conventional Stack might have started as a Contrarian Stack in the past, and today's Contrarian Stack might become tomorrow's Conventional Stack. Didn't Ruby on Rails initially emerge as an alternative to Java web development, and wasn't React once noticed as an alternative to older MVC frontend frameworks likeBackbone.js? In other words, I believe what's important isn't the specific technology itself, but rather maintaining curiosity that always looks toward new alternatives and making technical decisions based on your own judgment rather than simply delegating your choices to popular opinion.

Due to the limitations ofLLMs, where learning and reasoning are separated, Conventional Stacks will likely become even more conventional, and the disadvantages of Contrarian Stacks may grow. Claude Code can smoothly write Next.js code but struggles with SolidStart. Nevertheless, I believe the learning opportunities that only Contrarian Stacks can provide will remain valuable.

Even in the age ofLLMs, I will continue walking the contrarian path. This is because the learning opportunities provided by Contrarian Stacks go beyond simple knowledge acquisition—they foster a deeper understanding of technology. So I encourage you, the reader, to occasionally walk a path where Stack Overflow doesn't have the answers. The insights you gain at the end of that journey will become truly your own.

28
❤️
26
🎉
0
😂
0
😲
1
🤔
0
😢
0
👀
0
1
1
25
3

# 1 comment

If you have a fediverse account, you can comment on this article from your own instance. Searchhttps://hackers.pub/ap/articles/0197de66-6d9c-7728-abed-b8a4996f3022on your instance and reply to it.

Juntai Park

@arkjun@hackers.pub
7/7/2025, 5:53:08 AM
Quiet public

@hongminhee洪 民憙 (Hong Minhee)최대한 빨리 결과를 낼 수 있는(?) 스택을 선호하는 직업 개발자의 자세로 임하는 저를 반성하게 되네요. 좋은 글 잘 읽었습니다. 순수 즐거움을 찾아가는 개발자의 열정이 느껴져서 많이 배우게 됩니다. (저도 그런 때가있었는데없었어요) 감사합니다~. 😅

2
❤️
2
🎉
0
😂
0
😲
0
🤔
0
😢
0
👀
0
0
0
0
0
