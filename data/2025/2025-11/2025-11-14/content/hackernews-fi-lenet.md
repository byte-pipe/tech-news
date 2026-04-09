---
title: fi-le.net
url: https://fi-le.net/margin/
site_name: hackernews
fetched_at: '2025-11-14T19:06:53.481666'
original_url: https://fi-le.net/margin/
author: fi-le
date: '2025-11-14'
description: fi-le.net, the Fiefdom of Files
---

### The Fiefdom of Files

# Operating Margins

3rd of November 2025

Divide a company's income by its revenue, and you get the operating margin. For some volume of sales that comes into the business, it gives an idea of what percentage is left as cash in the end. Barring some accounting shenanigans regarding where the bottom line is.

The size of margins is often cited to explain how businesses behave: "Amazon was incentivized to move to cloud hosting and AWS as a higher-margin business than retail, whereas Google could not have been the first mover in hosting because advertising has higher margins." It's a compelling story, though hard to prove definitively as an important part of the company's behavior.

Here, let's instead look at some cold hard empirical data about operating margins of real companies. Usingeveryone's favorite websiteas the source, we get yearly operating margins of >10,000 public companies alongside business categories and market caps. We look at the last available year, 2025, and cluster by category.

 To summarize a category, we can straightforwardly take the median margin over all companies in the category. This produces some counterintuitive results, with for exampleSemiconductorsshowing a mediocre median margin of 10%. While this is a perfectly meaningful result, it obscures the fact that the category is dominated by a few large outlier companies with very high margins. And of course it's no coincidence that companies with high margins are the largest; those margins are what allowed them to grow in the first place, while their size conversely gives them pricing power and thus higher margins. We therefore also put in an average margin weighted by market cap. Using the weighted average,Semiconductorssits at an exceptional 42%.

Here is an interactive plot of median vs weighted average margins for each category, where the size of the dot is the total market cap of companies in the category.

The bulk of the companies sit at around a margin of 10%, but there are several clusters of categories with different numbers. Let's categorize those that achieve unusually high margins.

### Straight-Up Monopolies

All with an extremely high average margin of 49%, the categoriesToll Road Operators,Stock ExchangesandPortsstick out. What do all of them have in common? They are highly regulated monopolies, where even the permitting itself is enough to deter competitors. Ports and roads are based on quickly exhausted finite geographic resources; the first player to connect two points takes up the only viable land needed to complete the project. Some interesting examples are the largest company in Cambodia,Sihanoukville Autonomous Port, which is a literal government agency, orThe Cross-Harbour Holdings, which was tasked by the government of Hong Kong to build and maintain the first underwater tunnel of the country.Airportsare in a similar position, though showing slightly lower average margins of 42%, maybe because it's feasible to put a second airport next to an existing one to undercut the incumbent's prices. Interestingly, the classic example for monopolies,Utility Companies, are at only 17% average margin.

### Quasi-Monopolies

While it's not illegal to try and compete withNvidia(margin in 2025: 61%) orMastercard(margin in 2025: 54%), it's just so capital-intensive to catch up with their graphics card R&D / bank partner network that few companies are brave enough. These businesses are found in the upper-right quadrant of the graph, because the median company in the category is struggling hard to make money at smaller scales, whereas the returns to scale for the big players lead to high margins. This is the phenomenon we saw earlier for theSemiconductorscategory; some similar categories would beAIorNetworking Hardware.

### Weird Monopolies

In the middle of the graph, with higher average and median margins of around 15%, we findCementandBuilding Materials. This is counterintuitive because they are often low-tech and have high operating expenses. Apparently the story is that competitors are kept out of the business by the incumbent undercutting the new entrant until below cost, starving them of cash.Cruise Linesare also weirdly high at 16%, especially compared to airlines at 12%. Maybe it has to do with building relationships with shipbuilders or ports, or maybe the subset of cruise lines that are public is skewed.

### Just Slapping Your Name on Things

At an average and median of 20%,Pizzais one of the best categories out there, but presumably it has less to do with the pizza specifically, and more with the companies in this subset being franchisors. Since they don't actually operate stores, the franchisor companies are incredibly profitable. For comparison,LVMH, who want to sell you their tiny handbags for $2,000, had 21% margins in 2025. Even more amazing is theBeveragescategory with 29%.

### Actually Having Good Unit Economics

Zhejiang NHU Co., Ltd.is an example of just making a product that is worth much more than its raw materials, thus making a high profit. Being in theDietary Supplementscategory, they synthesize vitamins for both humans and factory-farmed animals, yielding a bloody 37% margin in 2025. Another surprising category isTool Manufacturersat 24% margins, which is presumably this high because the raw material costs are so much lower compared to the final specialized product. Unit economics would also explain why for instance gold mines have higher margins than silver mines. Perhaps the best illustration of the phenomenon areBanksorAsset Management, where the costs are by default low compared to the returns, even with abundant competition. In case you were wondering what the margins look like for literally printing money, they are as high as 99.5%—at least that is what theSwiss National Bankreported in 2024.

## By-Country Differences

Looking at the last available year of data for each company and calculating the weighted average by country, we see large discrepancies:

Country

Median Margin

Average Margin

Sample Size

South Africa
28.86%
82.37%
7

Indonesia
20.33%
44.11%
25

Qatar
22.63%
43.05%
37

Iceland
21.57%
42.52%
17

United Arab Emirates
53.13%
41.45%
23

Saudi Arabia
13.30%
40.73%
159

Philippines
31.29%
39.79%
12

Taiwan
16.80%
38.19%
74

Greece
25.96%
36.81%
35

Cambodia
33.72%
35.21%
4

Czech Republic
40.67%
35.17%
4

Malaysia
17.72%
33.48%
34

Singapore
16.82%
33.44%
49

Russia
24.53%
27.73%
13

Chile
24.35%
27.64%
10

Italy
11.27%
27.21%
135

Austria
6.41%
26.99%
48

Denmark
11.52%
25.72%
44

Brazil
12.19%
25.56%
81

Belgium
8.10%
25.37%
68

Australia
10.46%
24.74%
266

Sweden
8.97%
24.56%
175

Spain
9.04%
24.45%
93

China
10.49%
24.17%
255

Norway
13.33%
23.68%
64

Turkey
10.33%
23.05%
38

Poland
11.19%
22.96%
92

India
11.86%
22.76%
429

United States
7.20%
22.63%
2727

Hong Kong
6.52%
21.18%
87

United Kingdom
14.60%
21.18%
63

Thailand
18.82%
19.86%
43

Switzerland
11.32%
18.64%
165

Finland
7.21%
18.54%
80

Japan
9.73%
17.72%
583

Canada
7.77%
17.61%
301

France
6.72%
17.61%
283

Mexico
14.88%
17.46%
24

South Korea
7.52%
17.28%
108

Luxembourg
7.68%
16.54%
25

Bahrain
12.86%
15.60%
12

Vietnam
25.93%
14.68%
20

Argentina
12.43%
14.39%
18

Ireland
10.71%
14.03%
32

Portugal
9.99%
13.30%
19

Germany
6.47%
13.25%
305

Netherlands
6.73%
7.01%
55

New Zealand
3.50%
6.49%
35

Israel
3.33%
-8.97%
52

Show more rows

It's surprisingly hard to find a dominating pattern in the data. This is in part due to small per-country sample sizes and a selection bias regarding data availability; for example many of the countries high up on the list simply have many banks in the sample. However, we do see resource-heavy economies at the top, which is intuitive. One country is definitely the odd one out: Israel. Because of the relatively recent venture-funded startup ecosystem, we see so many unprofitable companies that the average margin is as low as -9%. It would be natural here to look for differences due to accounting standards in different countries, but it's certainly not obvious that this is an important aspect here. Perhaps the US median is a little bit lower than in other countries because of theGenerally Accepted Accounting Principlesstandard, which apparently allows for less leeway compared to theInternational Financial Reporting Standardsused in many other countries on the list.

## Upshot

It pays off to know the margin for any given business you are interfacing with; all things being equal, you probably want to be in a higher margin situation. Here we looked at some basic patterns in worldwide company data, identifying some interesting types of businesses that stand out in this regard.This is the second entry in a mini series, following a previous one identifying themost silly companies.

## Appendix

The by-category margins are repeated in this table.CategoryMedian MarginWeighted Avg. MarginPorts49.03%49.11%Stock/Crypto Exchanges45.14%49.64%Stock Exchanges45.08%49.91%Banks35.87%38.11%Toll Road Operators34.21%49.47%Financial Services32.77%38.78%Asset Management31.48%24.18%Airports30.93%42.13%Railways27.20%32.38%Infrastructure26.94%29.54%Container Shipping25.23%25.45%Investment24.16%28.68%Maritime Transportation23.71%24.55%Tobacco23.55%40.30%Reits22.37%26.82%Real Estate21.82%24.58%Gold Mining20.88%40.12%Pizza20.11%20.30%Dow Jones19.12%34.81%Tool Manufacturers18.62%24.41%Flavors & Fragrances18.48%10.93%Tools And Hardware18.48%18.65%Pollution Control And Treatment17.75%22.84%Cement17.06%14.47%Cruise Lines16.03%16.04%Silver Mining15.54%37.34%Utility Companies15.02%17.85%Online Travel14.58%23.18%Building Materials14.52%15.15%Fertilizer Companies14.29%16.76%Cac 4014.15%16.33%Electricity13.72%15.25%Paint & Coating13.50%13.13%Oil & Gas12.98%23.24%Insurance12.94%14.67%Alcoholic Beverages12.92%42.81%Intellectual Property & Patent Licensing12.76%19.49%Beverages12.70%29.30%Consumer Goods12.37%19.05%Rental & Leasing Services12.34%15.01%Travel11.96%20.56%Energy11.94%20.54%Wellness11.82%10.74%Hotels11.80%15.27%Car Rental11.15%-0.08%Conglomerate11.09%15.01%Hospitality10.79%10.79%Semiconductors10.05%42.11%Mining10.04%27.42%Transportation10.01%18.87%Motorcycle Manufacturers9.67%11.81%Dietary Supplements9.51%27.96%Telecommunication9.44%14.21%Education9.38%12.96%Defense Contractors9.37%12.35%Media/Press9.37%15.46%Dairy Companies9.35%7.57%Machinery Manufacturing9.18%17.68%Medical Care Facilities9.16%13.34%Gambling9.02%14.19%Esports8.86%27.16%Aluminum8.72%12.55%Toys8.66%11.31%Agriculture8.58%10.94%Medical Equipment8.50%18.36%Luxury Goods8.38%10.22%Home & Kitchen Appliances8.17%13.56%Pulp And Paper8.02%13.76%Entertainment7.79%12.80%Clothing7.68%13.21%Construction7.67%13.31%Professional Services7.63%18.50%Airlines7.50%12.04%Waste & Recycling7.47%12.85%Dax7.44%13.89%Electronics7.36%38.53%Engineering7.31%11.38%Scientific & Technical Instruments7.23%18.16%Security & Protection Services7.18%11.22%Video Games6.99%37.79%Packaging6.96%8.24%Manufacturing6.83%10.07%Tires6.81%9.13%Aerospace6.80%12.03%IT Services6.80%18.58%Oil & Gas Equipment & Services6.78%11.63%Restaurant Chains6.74%28.77%Led Lighting Manufacturers6.71%6.45%Aircraft Manufacturers6.54%3.93%Sports Goods6.35%9.79%Specialty Vehicles6.31%10.86%Furniture6.14%10.06%Food5.96%13.81%Tech Hardware5.88%35.80%Courier5.86%8.31%Staffing & Employment Services5.58%14.60%Drugstore5.37%2.15%Footwear5.30%9.66%Steel Industry5.30%7.43%Steel Producers5.15%6.35%Cosmetics & Beauty5.14%5.44%Gloves & PPE5.12%18.91%Automotive Suppliers5.11%10.50%Healthcare5.04%5.71%Automakers4.93%7.34%Auto Parts4.50%14.18%Chemicals4.48%11.07%Networking Hardware4.21%28.10%Multi-Level Marketing4.05%4.70%Supermarket Chains3.86%4.05%Retail3.82%9.60%Personal Care3.72%3.72%Tech3.69%29.23%Food Delivery3.62%3.98%Software3.50%29.15%Industrial Supplies3.22%3.22%Football3.18%-3.56%Telecommunications Equipment3.14%19.50%Internet3.04%26.33%Car Retail2.88%16.46%Ridesharing2.82%10.95%Advertising2.47%11.00%Coal Mining2.21%10.46%Eyewear1.83%8.97%Used Car Retailer1.67%19.04%Iot1.33%-4.75%E-Commerce0.83%13.02%Renewable Energy0.81%12.53%Recommerce0.03%-3.93%Bitcoin0.00%9.07%IT Security-0.01%5.98%Telehealth-0.06%19.63%Batteries-0.07%9.84%Cannabis-1.76%-15.99%Medical Devices-2.71%18.34%Pharmaceuticals-3.32%7.99%Online Dating-5.72%4.72%AI-6.40%39.65%Biotech-7.16%7.62%Autonomous Driving-7.18%43.79%Diagnostics And Testing-8.80%7.30%Biofuel-9.12%-6.33%3D Printing-14.67%-19.89%Glassware-15.05%-15.05%Bitcoin Mining-17.23%-43.59%Electric Vehicles-20.75%5.88%Robotics-20.75%-4.16%Ev Charging-41.25%8.59%Uranium-43.82%-10.23%Aircraft Leasing-53.55%34.11%Mrna Therapeutics-59.71%-81.28%Lidar-73.04%-38.92%Genomics-113.57%-75.48%Hydrogen Fuel Cell-168.57%-237.06%Gene Therapy-381.51%-336.75%Crispr-659.31%-337.66%Show more rows

 © 2021 - 2025
fi-le.net,

t
he fiefdom of files
 |
RSS
 |
 Newsletter Signup:
