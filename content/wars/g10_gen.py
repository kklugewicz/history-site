#!/usr/bin/env python3
"""Generator for wars_g10.json (group g10). Edit data here, then run: python3 g10_gen.py"""
import json, os, re

H = os.path.dirname(os.path.abspath(__file__))
BLUE, RED, GREEN = '#3b6fb6', '#c0473a', '#3f8f5a'


def side(name, color, leaders):
    return {'name': name, 'color': color, 'leaders': leaders}


def th(lon, lat, r):
    return {'lon': lon, 'lat': lat, 'r': r}


def terr(*groups):
    return [{'side': i, 'polities': p} for i, p in groups if p]


def fr(label, path):
    return {'path': path, 'label': label}


def mv(s, commander, label, path):
    return {'side': s, 'commander': commander, 'label': label, 'path': path}


def ev(name, kind, lon, lat, year, winner, text):
    return {'name': name, 'kind': kind, 'lon': lon, 'lat': lat, 'year': year, 'winner': winner, 'text': text}


def step(year, label, title, text, territories, fronts, moves, events):
    return {'year': year, 'label': label, 'title': title, 'text': text, 'territories': territories,
            'fronts': fronts, 'moves': moves, 'events': events}


def war(id, name, start, end, kind, summary, sides, theater, steps):
    return {'id': id, 'name': name, 'start': start, 'end': end, 'kind': kind, 'summary': summary,
            'sides': sides, 'theater': theater, 'steps': steps}


WARS = []

# ---------------------------------------------------------------- 1. Taiping Rebellion
QING = ['Manchu Empire']
WARS.append(war(
    'taiping-rebellion', 'Taiping Rebellion', 1850, 1864, 'war',
    "Hong Xiuquan, who believed he was the younger brother of Jesus, led the Taiping Heavenly Kingdom in a revolt "
    "against the Qing dynasty that captured Nanjing and much of the Yangtze valley. New regional Qing armies, above all "
    "Zeng Guofan's Xiang Army and Li Hongzhang's Huai Army, aided late in the war by Western-officered forces, crushed the "
    "rebellion in 1864. With perhaps 20 to 30 million dead it was one of the deadliest wars in history, and it shifted "
    "power from the Qing court to regional strongmen.",
    [side('Qing dynasty', BLUE, ['Zeng Guofan', 'Zeng Guoquan', 'Li Hongzhang', 'Zuo Zongtang', 'Senggelinqin', 'Charles Gordon']),
     side('Taiping Heavenly Kingdom', RED, ['Hong Xiuquan', 'Yang Xiuqing', 'Shi Dakai', 'Li Xiucheng', 'Chen Yucheng'])],
    [th(112.0, 26.5, 5.5), th(117.5, 31.0, 4.5), th(116.0, 37.0, 3)],
    [
        step(1851, 'Jan 1851', 'The Jintian Uprising',
             "Hong Xiuquan's God Worshipping Society gathered thousands of poor Hakka farmers and miners at Jintian in "
             "Guangxi and beat the Qing troops sent against them. In January 1851 Hong proclaimed the Taiping Heavenly "
             "Kingdom, and the rebels moved north to the walled town of Yong'an, where Qing armies besieged them.",
             terr((0, QING)), [],
             [mv(1, 'Hong Xiuquan', "March to Yong'an", [[110.1, 23.5], [110.3, 23.85], [110.52, 24.2]]),
              mv(0, 'Xiang Rong', "Qing troops close on Yong'an", [[110.29, 25.27], [110.45, 24.75], [110.52, 24.3]])],
             [ev('Jintian Uprising', 'event', 110.1, 23.5, 1851, 1,
                 "The rebels beat off Qing forces and proclaimed their Heavenly Kingdom.")]),
        step(1852, '1852 to 1853', 'March to Nanjing',
             "Breaking out of Yong'an, the Taiping marched north through Hunan, losing their leaders Feng Yunshan and "
             "Xiao Chaogui and failing to take Changsha, but gathering hundreds of thousands of recruits. They seized "
             "Wuchang, sailed down the Yangtze and captured Nanjing in March 1853, making it their Heavenly Capital, "
             "with Qing armies trailing behind.",
             terr((0, QING)), [],
             [mv(1, 'Yang Xiuqing', 'Taiping advance down the Yangtze',
                 [[110.52, 24.2], [110.29, 25.27], [112.94, 28.23], [114.3, 30.55], [117.05, 30.52], [118.78, 32.05]]),
              mv(0, 'Xiang Rong', 'Qing pursuit to Nanjing',
                 [[110.29, 25.3], [112.9, 28.0], [114.2, 30.4], [117.0, 30.4], [118.9, 32.0]])],
             [ev('Siege of Changsha', 'siege', 112.94, 28.23, 1852, 0,
                 "The Qing garrison held the city and the Taiping leader Xiao Chaogui was killed."),
              ev('Capture of Wuchang', 'siege', 114.3, 30.55, 1853, 1,
                 "The Taiping took their first provincial capital and its river boats."),
              ev('Capture of Nanjing', 'siege', 118.78, 32.05, 1853, 1,
                 "Nanjing fell and became the Taiping capital, Tianjing.")]),
        step(1853, '1853 to 1855', 'Northern and Western Expeditions',
             "A Taiping army marched north to take Beijing and reached the outskirts of Tianjin, but froze and starved "
             "and was destroyed by the Mongol cavalry of Senggelinqin. A Western Expedition fought up the Yangtze "
             "against Zeng Guofan's new Hunan militia, the Xiang Army, which won at Xiangtan but had its river fleet "
             "smashed at Hukou. Qing camps sat outside Nanjing and Yangzhou without being able to take the capital.",
             terr((0, QING)),
             [fr('Qing Jiangnan and Jiangbei camps', [[119.42, 32.42], [119.1, 32.25], [118.95, 32.05], [118.88, 31.88]])],
             [mv(1, 'Lin Fengxiang and Li Kaifang', 'Northern Expedition',
                 [[118.78, 32.1], [115.78, 33.85], [114.35, 34.8], [115.5, 36.6], [116.9, 38.9]]),
              mv(1, 'Shi Dakai', 'Western Expedition', [[118.78, 32.05], [117.05, 30.52], [116.0, 29.7], [114.3, 30.55]]),
              mv(0, 'Zeng Guofan', 'Xiang Army down the Xiang River', [[112.94, 28.23], [113.1, 29.37], [114.3, 30.55], [116.1, 29.75]]),
              mv(0, 'Senggelinqin', 'Qing cavalry from Beijing', [[116.4, 39.9], [116.6, 38.9], [116.55, 37.9]])],
             [ev('Battle of Xiangtan', 'battle', 112.94, 27.83, 1854, 0,
                 "Zeng Guofan's Xiang Army won its first great victory and saved Hunan."),
              ev('Fall of Lianzhen', 'siege', 116.55, 37.9, 1855, 0,
                 "Senggelinqin captured the last Northern Expedition leaders and ended the threat to Beijing."),
              ev('Battle of Hukou', 'battle', 116.21, 29.74, 1855, 1,
                 "Shi Dakai trapped and smashed Zeng Guofan's river fleet at the mouth of Poyang Lake.")]),
        step(1856, '1856', 'Victory and the Tianjing Incident',
             "Taiping armies under Shi Dakai and Qin Rigang destroyed the Qing Jiangnan camp besieging Nanjing, and the "
             "Heavenly Kingdom reached the height of its power. Weeks later a power struggle in Nanjing, the Tianjing "
             "Incident, saw the Eastern King Yang Xiuqing and thousands of his followers killed, and in 1857 Shi Dakai "
             "left with his army, never to return.",
             terr((0, QING)), [],
             [mv(1, 'Shi Dakai', 'Relief of Nanjing', [[115.89, 28.68], [117.0, 30.5], [118.3, 31.4], [118.85, 32.05]]),
              mv(1, 'Shi Dakai', 'Breaks away to the west (1857)', [[118.78, 32.05], [117.05, 30.52], [115.9, 28.7], [111.5, 26.4], [104.0, 28.0]])],
             [ev('Jiangnan Great Camp', 'battle', 118.95, 32.03, 1856, 1,
                 "Taiping armies destroyed the Qing siege camp east of Nanjing."),
              ev('Tianjing Incident', 'event', 118.78, 32.06, 1856, None,
                 "Hong Xiuquan's lieutenants slaughtered Yang Xiuqing and his followers, crippling the leadership.")]),
        step(1858, '1858 to 1860', 'Revival under Li Xiucheng',
             "New commanders Chen Yucheng and Li Xiucheng restored Taiping fortunes, wiping out a Xiang Army force at "
             "Sanhe. In 1860 they broke the rebuilt Qing siege of Nanjing and swept east to take Suzhou, but were turned "
             "back at Shanghai by Qing troops, British and French soldiers and Frederick Townsend Ward's foreign-led militia.",
             terr((0, QING)),
             [fr('Xiang Army front in Anhui, 1860', [[115.8, 31.6], [116.5, 30.95], [116.95, 30.4]])],
             [mv(1, 'Li Xiucheng', 'Eastern campaign', [[118.78, 32.05], [119.95, 31.78], [120.62, 31.3], [121.25, 31.25]]),
              mv(1, 'Chen Yucheng', 'Strikes the Xiang Army in Anhui', [[118.4, 31.7], [117.7, 31.6], [117.25, 31.5]]),
              mv(0, 'Zeng Guofan', 'Xiang Army closes on Anqing', [[115.95, 29.7], [116.3, 30.2], [116.9, 30.5]])],
             [ev('Battle of Sanhe', 'battle', 117.25, 31.5, 1858, 1,
                 "Chen Yucheng and Li Xiucheng annihilated Li Xubin's Xiang Army force."),
              ev('Capture of Suzhou', 'siege', 120.62, 31.3, 1860, 1,
                 "The Taiping captured the rich city of Suzhou after breaking the Jiangnan siege."),
              ev('Defence of Shanghai', 'battle', 121.47, 31.23, 1860, 0,
                 "Qing and Western troops held Shanghai against Li Xiucheng.")]),
        step(1861, '1861 to 1863', 'Anqing falls, Shanghai holds',
             "Zeng Guofan's brother Zeng Guoquan starved Anqing into surrender in 1861, opening the way down the "
             "Yangtze to Nanjing. Li Hongzhang's Huai Army and the Ever Victorious Army, later led by Charles Gordon, "
             "cleared the country around Shanghai and retook Suzhou in late 1863, while Zuo Zongtang's army fought its "
             "way into Zhejiang.",
             terr((0, QING)),
             [fr('Shanghai defence zone', [[121.1, 30.9], [120.95, 31.25], [121.2, 31.6]])],
             [mv(0, 'Zeng Guoquan', 'Xiang Army down the Yangtze', [[117.05, 30.52], [118.38, 31.33], [118.78, 32.0]]),
              mv(0, 'Li Hongzhang and Charles Gordon', 'Huai Army and Ever Victorious Army', [[121.47, 31.23], [120.98, 31.38], [120.62, 31.3]]),
              mv(0, 'Zuo Zongtang', 'Chu Army into Zhejiang', [[117.9, 28.45], [119.0, 29.1], [120.16, 30.25]])],
             [ev('Siege of Anqing', 'siege', 117.05, 30.52, 1861, 0,
                 "The Xiang Army starved Anqing into surrender, the decisive turning point."),
              ev('Recapture of Suzhou', 'siege', 120.62, 31.3, 1863, 0,
                 "Li Hongzhang and Gordon's forces retook Suzhou, and the surrendered Taiping leaders were executed.")]),
        step(1864, 'Jun to Jul 1864', 'Fall of Nanjing',
             "With Nanjing encircled and starving, Hong Xiuquan died in June 1864. The Xiang Army blew a breach in the "
             "walls in July and massacred much of the population; Li Xiucheng was caught and executed, and the "
             "remaining Taiping bands were hunted down over the next few years.",
             terr((0, QING)),
             [fr('Siege lines around Nanjing', [[118.65, 32.15], [118.95, 32.12], [118.97, 31.98], [118.72, 31.95], [118.65, 32.05]])],
             [mv(0, 'Zeng Guoquan', 'Storm of Nanjing', [[118.6, 31.85], [118.75, 31.98], [118.8, 32.05]])],
             [ev('Third Battle of Nanjing', 'siege', 118.8, 32.06, 1864, 0,
                 "The Xiang Army stormed the Taiping capital and ended the Heavenly Kingdom.")]),
    ]))

# ---------------------------------------------------------------- 2. Indian Rebellion of 1857
CO = ['British East India Company']
WARS.append(war(
    'indian-rebellion-1857', 'Indian Rebellion of 1857', 1857, 1858, 'war',
    "In 1857 sepoys of the East India Company's Bengal Army mutinied at Meerut, and the revolt spread across the Ganges "
    "plain and central India, joined by dispossessed rulers, landholders and peasants who rallied around the Mughal emperor "
    "Bahadur Shah II. Company forces, reinforced from Britain and helped by loyal Sikh, Gurkha and princely troops, retook "
    "Delhi, Lucknow and central India by mid 1858, with atrocities and brutal reprisals on both sides. The British Crown "
    "then abolished Company rule and governed India directly as the British Raj.",
    [side('East India Company and loyal forces', RED, ['Colin Campbell', 'Hugh Rose', 'Henry Havelock', 'John Nicholson', 'James Outram']),
     side('Rebel sepoys and allied rulers', GREEN, ['Bahadur Shah II', 'Nana Sahib', 'Rani Lakshmibai', 'Tantia Tope', 'Begum Hazrat Mahal'])],
    [th(79.5, 26.5, 4.5)],
    [
        step(1857, 'May 1857', 'Mutiny at Meerut',
             "Anger at new rifle cartridges said to be greased with cow and pig fat, and at years of annexations, burst "
             "out at Meerut on 10 May 1857, when sepoys freed their jailed comrades and killed British officers and "
             "civilians. They rode overnight to Delhi, where the garrison joined them and the aged Mughal emperor "
             "Bahadur Shah II was proclaimed their leader. Within weeks regiments across the Ganges plain and Awadh had risen.",
             terr((0, CO), (1, ['Oudh'])), [],
             [mv(1, '3rd Bengal Light Cavalry', 'Meerut mutineers ride to Delhi', [[77.7, 28.98], [77.45, 28.82], [77.24, 28.66]]),
              mv(0, 'General Anson', 'Delhi Field Force from Ambala', [[76.78, 30.38], [77.0, 29.7], [77.15, 28.74]])],
             [ev('Meerut mutiny', 'event', 77.7, 28.98, 1857, 1,
                 "Sepoys of the Bengal Army rose, killed their officers and marched on Delhi."),
              ev('Bahadur Shah II proclaimed', 'event', 77.24, 28.66, 1857, 1,
                 "The rebels restored the last Mughal emperor as the figurehead of the revolt.")]),
        step(1857, 'Jun to Aug 1857', 'Cawnpore, Lucknow and the Delhi Ridge',
             "A small British force camped on the ridge outside Delhi, too weak to attack the city. At Cawnpore Nana "
             "Sahib's forces besieged General Wheeler's entrenchment, and its surrendered garrison and then the women and "
             "children were massacred; Henry Havelock's column fought its way up from Allahabad and retook the town in "
             "July. In Lucknow the British Residency was besieged from 1 July.",
             terr((0, CO), (1, ['Oudh'])),
             [fr('Delhi Ridge', [[77.19, 28.70], [77.205, 28.68], [77.215, 28.665]]),
              fr('Lucknow Residency siege', [[80.92, 26.87], [80.94, 26.865], [80.935, 26.855]])],
             [mv(1, 'Nana Sahib', 'Rebels besiege Cawnpore', [[80.27, 26.61], [80.3, 26.52], [80.33, 26.46]]),
              mv(0, 'Henry Havelock', 'Relief column from Allahabad', [[81.85, 25.44], [80.81, 25.93], [80.33, 26.45]]),
              mv(1, 'Begum Hazrat Mahal', 'Awadh rebels besiege Lucknow', [[81.2, 26.75], [81.05, 26.82], [80.94, 26.86]])],
             [ev('Siege of Cawnpore', 'siege', 80.33, 26.46, 1857, 1,
                 "Wheeler's entrenchment surrendered and its people were killed at Satichaura Ghat and Bibighar."),
              ev('Siege of Lucknow begins', 'siege', 80.93, 26.86, 1857, None,
                 "About 1,700 soldiers and loyal sepoys held the Residency against far larger rebel forces.")]),
        step(1857, 'Sep to Dec 1857', 'Delhi stormed, Lucknow relieved',
             "Reinforced by John Nicholson's column and siege guns from the Punjab, the British stormed Delhi on 14 "
             "September and took it after a week of street fighting; Nicholson was killed and Bahadur Shah was captured. "
             "Havelock and Outram broke into the Lucknow Residency but were trapped there until Sir Colin Campbell "
             "evacuated it in November, then beat Tantia Tope's Gwalior Contingent at Cawnpore.",
             terr((0, CO), (1, ['Oudh'])),
             [fr('Lucknow Residency siege', [[80.92, 26.87], [80.94, 26.865], [80.935, 26.855]])],
             [mv(0, 'John Nicholson', 'Movable Column from the Punjab', [[74.34, 31.55], [75.85, 30.9], [76.78, 30.38], [77.21, 28.68]]),
              mv(0, 'Colin Campbell', 'Second relief of Lucknow', [[80.33, 26.45], [80.6, 26.7], [80.94, 26.86]]),
              mv(1, 'Tantia Tope', 'Gwalior Contingent on Cawnpore', [[79.73, 26.12], [80.05, 26.3], [80.33, 26.46]])],
             [ev('Siege of Delhi', 'siege', 77.23, 28.66, 1857, 0,
                 "The British stormed the Kashmiri Gate and retook the Mughal capital."),
              ev('Relief of Lucknow', 'siege', 80.94, 26.86, 1857, 0,
                 "Campbell fought through to the Residency and evacuated its garrison and civilians."),
              ev('Second Battle of Cawnpore', 'battle', 80.35, 26.47, 1857, 0,
                 "Campbell routed Tantia Tope's army outside Cawnpore.")]),
        step(1858, 'Mar 1858', 'Lucknow retaken',
             "With fresh British regiments arriving, Campbell returned to Lucknow with some 30,000 men and Gurkha allies "
             "from Nepal and took the city in March 1858 after two weeks of fighting. Begum Hazrat Mahal and thousands of "
             "rebels escaped into the Awadh countryside and Rohilkhand, which Campbell spent the summer clearing.",
             terr((0, CO), (1, ['Oudh'])), [],
             [mv(0, 'Colin Campbell', 'Advance on Lucknow', [[80.33, 26.45], [80.6, 26.7], [80.95, 26.85]]),
              mv(1, 'Begum Hazrat Mahal', 'Rebels scatter north', [[80.95, 26.85], [81.3, 27.4], [81.6, 28.0]])],
             [ev('Capture of Lucknow', 'siege', 80.95, 26.85, 1858, 0,
                 "Campbell stormed the rebel-held city and broke the main rebel army of Awadh.")]),
        step(1858, 'Mar to Jun 1858', 'The Central India campaign',
             "Sir Hugh Rose's Central India Field Force marched north from Mhow, stormed Jhansi in April after defeating "
             "a relief army under Tantia Tope, and took Kalpi in May. Rani Lakshmibai of Jhansi and Tantia Tope then "
             "seized the fortress of Gwalior, but Rose retook it in June and the Rani was killed fighting in cavalry dress.",
             terr((0, CO), (1, ['Oudh'])), [],
             [mv(0, 'Hugh Rose', 'Central India Field Force', [[75.77, 22.55], [78.74, 23.84], [78.57, 25.45], [79.73, 26.12], [78.18, 26.22]]),
              mv(1, 'Rani Lakshmibai and Tantia Tope', 'Rebels seize Gwalior', [[79.73, 26.12], [79.0, 26.2], [78.18, 26.22]])],
             [ev('Siege of Jhansi', 'siege', 78.57, 25.45, 1858, 0,
                 "Rose stormed the fortress, and the Rani escaped over the walls."),
              ev('Battle of Gwalior', 'battle', 78.18, 26.22, 1858, 0,
                 "The rebels lost their last great stronghold and Rani Lakshmibai was killed.")]),
        step(1858, 'Aug 1858 to Apr 1859', 'Crown rule',
             "The Government of India Act of August 1858 ended the East India Company's rule, and on 1 November Queen "
             "Victoria's proclamation promised religious tolerance and pardons to most rebels. Tantia Tope led his "
             "pursuers on a long chase through Rajputana and central India until he was betrayed and hanged in April "
             "1859, while Begum Hazrat Mahal and Nana Sahib fled into Nepal.",
             terr((0, CO + ['Oudh'])), [],
             [mv(1, 'Tantia Tope', 'Guerrilla flight', [[78.18, 26.22], [76.5, 25.2], [74.6, 24.0], [74.8, 22.8], [77.0, 23.2], [77.65, 25.43]])],
             [ev("Queen Victoria's Proclamation", 'event', 81.85, 25.44, 1858, 0,
                 "Read at Allahabad, it announced direct rule by the Crown over India."),
              ev('Execution of Tantia Tope', 'event', 77.65, 25.43, 1859, 0,
                 "The last major rebel commander was captured and hanged at Shivpuri.")]),
    ]))

# ---------------------------------------------------------------- 3. Wars of German Unification
NORTH = ['Prussia', 'Hohenzollern', 'Wetzlar', 'Schleswig', 'Holstein', 'Mecklenburg-Schwerin', 'Mecklenburg-Strelitz',
         'Oldenburg', 'Brunswick', 'Anhalt', 'Waldeck', 'Lippe-Detmold', 'Schaumburg-Lippe', 'Hamburg', 'Bremen', 'Lübeck']
ITALY = ['Kingdom of Sardinia', 'Lombardy', 'Tuscany', 'Modena', 'Parma', 'Lucca', 'Massa', 'Fivizzano', 'Pontremoli',
         'Kingdom of the Two Sicilies']
AUSTRIA66 = ['Austrian Empire', 'Venetia', 'Saxony', 'Bavaria', 'Palatinate', 'Württemberg', 'Baden', 'Hanover',
             'Electoral Hesse', 'Grand Duchy of Hesse', 'Nassau']
GERMANY70 = NORTH + ['Hanover', 'Electoral Hesse', 'Nassau', 'Saxony', 'Thuringia', 'Bavaria', 'Palatinate',
                     'Württemberg', 'Baden', 'Grand Duchy of Hesse']
PARIS_RING = [[2.12, 48.97], [2.45, 49.0], [2.62, 48.86], [2.45, 48.72], [2.2, 48.74], [2.1, 48.85], [2.12, 48.97]]
WARS.append(war(
    'wars-of-german-unification', 'Wars of German Unification', 1864, 1871, 'conflict',
    "Between 1864 and 1871 Prussia, steered by its minister-president Otto von Bismarck and its chief of staff Helmuth "
    "von Moltke, fought three short wars, against Denmark, Austria and France. Each was quick and decisive, and together "
    "they pushed Austria out of German affairs and drew the southern German states into a Prussian-led union. The German "
    "Empire proclaimed at Versailles in January 1871 became the strongest power on the continent, while France's loss of "
    "Alsace and Lorraine left a lasting grievance.",
    [side('Prussia and its allies', BLUE, ['Otto von Bismarck', 'Helmuth von Moltke', 'King Wilhelm I', 'Crown Prince Friedrich Wilhelm', 'Prince Friedrich Karl']),
     side("Prussia's opponents (Denmark, Austria, France)", RED, ['Christian de Meza', 'Ludwig von Benedek', 'Napoleon III', 'Marshal Bazaine', 'Marshal MacMahon'])],
    [th(11.5, 51.0, 6.5), th(4.0, 48.9, 3.5)],
    [
        step(1864, 'Feb to Oct 1864', 'Second Schleswig War',
             "When Denmark tied the duchy of Schleswig more closely to the Danish crown, Prussia and Austria invaded in "
             "February 1864. The Danes abandoned their Danevirke line, the Prussians stormed the Dybbøl redoubts in "
             "April and Austrian troops pushed up into Jutland. In the Treaty of Vienna Denmark gave up Schleswig, "
             "Holstein and Lauenburg to joint Austro-Prussian rule.",
             terr((0, ['Prussia', 'Austrian Empire', 'Venetia', 'Schleswig', 'Holstein']), (1, ['Denmark'])),
             [fr('Danevirke line, Feb 1864', [[9.4, 54.43], [9.52, 54.46], [9.6, 54.51], [9.85, 54.62]]),
              fr('Dybbøl redoubts, Apr 1864', [[9.71, 54.94], [9.73, 54.91], [9.75, 54.89]])],
             [mv(0, 'Prince Friedrich Karl', 'Prussians to Dybbøl', [[10.13, 54.32], [9.9, 54.6], [9.72, 54.9]]),
              mv(0, 'Ludwig von Gablenz', 'Austrians into Jutland', [[9.94, 53.6], [9.55, 54.45], [9.43, 54.78], [9.47, 55.49], [9.53, 55.71]]),
              mv(1, 'Christian de Meza', 'Danish retreat from the Danevirke', [[9.55, 54.47], [9.43, 54.78], [9.75, 54.9]])],
             [ev('Battle of Dybbøl', 'battle', 9.73, 54.91, 1864, 0,
                 "Prussian infantry stormed the Danish redoubts after a long bombardment, deciding the war."),
              ev('Treaty of Vienna', 'treaty', 16.37, 48.21, 1864, 0,
                 "Denmark ceded Schleswig, Holstein and Lauenburg to Prussia and Austria.")]),
        step(1866, 'Jun to Aug 1866', 'Austro-Prussian War',
             "Prussia and Austria fell out over the duchies and over leadership of Germany, and most German states sided "
             "with Austria. While a Prussian army knocked out Hanover and the southern states in the west, Moltke sent "
             "three armies by rail and road into Bohemia, where they converged on Benedek's Austrians and crushed them "
             "at Königgrätz on 3 July. Italy, Prussia's ally, was beaten at Custoza but still gained Venetia, and the "
             "Peace of Prague let Prussia annex Hanover, Hesse-Kassel, Nassau and Frankfurt and lead a new North German "
             "Confederation without Austria.",
             terr((0, NORTH + ITALY), (1, AUSTRIA66)),
             [fr('Austrian line at Königgrätz, 3 Jul', [[15.72, 50.38], [15.76, 50.3], [15.8, 50.22]])],
             [mv(0, 'Herwarth von Bittenfeld', 'Elbe Army', [[13.74, 51.05], [14.6, 50.6], [15.35, 50.44], [15.68, 50.3]]),
              mv(0, 'Prince Friedrich Karl', 'First Army', [[14.99, 51.15], [15.05, 50.77], [15.35, 50.44], [15.7, 50.33]]),
              mv(0, 'Crown Prince Friedrich Wilhelm', 'Second Army from Silesia', [[16.65, 50.6], [16.16, 50.41], [15.9, 50.38], [15.82, 50.33]]),
              mv(1, 'Ludwig von Benedek', 'Austrian North Army', [[17.25, 49.6], [16.5, 49.95], [15.83, 50.25]]),
              mv(0, 'Vogel von Falckenstein', 'Army of the Main', [[9.74, 52.37], [10.65, 51.11], [10.07, 50.2], [8.68, 50.11]])],
             [ev('Battle of Königgrätz', 'battle', 15.68, 50.3, 1866, 0,
                 "The three Prussian armies met on the battlefield and routed the Austrians, deciding the war in a day."),
              ev('Battle of Custoza', 'battle', 10.8, 45.38, 1866, 1,
                 "Austria's southern army beat the Italians, but could not change the outcome in Bohemia."),
              ev('Peace of Prague', 'treaty', 14.42, 50.08, 1866, 0,
                 "Austria accepted the end of the German Confederation and Prussian leadership of the north.")]),
        step(1870, 'Jul to Aug 1870', 'France goes to war',
             "Bismarck's edited Ems Dispatch goaded Napoleon III into declaring war in July 1870, and the southern German "
             "states joined Prussia as their treaties required. Moltke's armies mobilised faster, beat MacMahon in Alsace "
             "at Wörth and broke into Lorraine. After the bloody battles of Mars-la-Tour and Gravelotte, Bazaine's Army "
             "of the Rhine was shut up inside the fortress of Metz.",
             terr((0, GERMANY70), (1, ['France'])),
             [fr('Metz encircled, Aug 1870', [[6.05, 49.2], [6.3, 49.22], [6.33, 49.05], [6.1, 49.0], [6.0, 49.1], [6.05, 49.2]])],
             [mv(0, 'Crown Prince Friedrich Wilhelm', 'Third Army into Alsace', [[8.12, 49.2], [7.94, 49.04], [7.74, 48.94], [6.18, 48.69], [5.16, 48.77]]),
              mv(0, 'Prince Friedrich Karl', 'Second Army on Metz', [[7.36, 49.25], [6.6, 49.0], [6.06, 48.9], [5.9, 49.08]]),
              mv(0, 'Karl von Steinmetz', 'First Army', [[6.99, 49.23], [6.6, 49.15], [6.05, 49.12]]),
              mv(1, 'Marshal MacMahon', 'Retreat from Alsace', [[7.74, 48.94], [6.5, 48.59], [5.6, 48.65], [4.36, 48.96]]),
              mv(1, 'Marshal Bazaine', 'Army of the Rhine falls back on Metz', [[6.9, 49.19], [6.5, 49.13], [6.18, 49.12]])],
             [ev('Ems Dispatch', 'event', 7.71, 50.33, 1870, None,
                 "Bismarck's sharpened version of a royal telegram provoked France into declaring war."),
              ev('Battle of Wörth', 'battle', 7.74, 48.94, 1870, 0,
                 "The Crown Prince's Third Army routed MacMahon and opened Alsace."),
              ev('Battle of Gravelotte', 'battle', 6.03, 49.11, 1870, 0,
                 "The largest battle of the war forced Bazaine back into Metz.")]),
        step(1870, 'Aug to Sep 1870', 'Sedan',
             "MacMahon, with Napoleon III riding with him, marched the new Army of Châlons north east to relieve Metz. "
             "Moltke wheeled his armies north, cornered it against the Belgian border at Sedan and pounded it from the "
             "surrounding heights. On 2 September the emperor and over 100,000 men surrendered; two days later Paris "
             "overthrew the Empire and proclaimed the Third Republic.",
             terr((0, GERMANY70), (1, ['France'])),
             [fr('Sedan pocket, 1 Sep 1870', [[4.87, 49.75], [5.0, 49.76], [5.03, 49.68], [4.93, 49.65], [4.87, 49.75]]),
              fr('Metz encircled', [[6.05, 49.2], [6.3, 49.22], [6.33, 49.05], [6.1, 49.0], [6.0, 49.1], [6.05, 49.2]])],
             [mv(1, 'Marshal MacMahon', 'Army of Châlons', [[4.36, 48.96], [4.03, 49.26], [4.37, 49.51], [4.94, 49.7]]),
              mv(0, 'Crown Prince Friedrich Wilhelm', 'Third Army wheels north', [[5.16, 48.77], [4.9, 49.15], [4.86, 49.55], [4.92, 49.68]]),
              mv(0, 'Crown Prince Albert of Saxony', 'Army of the Meuse', [[5.38, 49.16], [5.2, 49.45], [5.05, 49.65], [4.98, 49.72]])],
             [ev('Battle of Sedan', 'battle', 4.94, 49.7, 1870, 0,
                 "Napoleon III and the Army of Châlons surrendered, bringing down the Second Empire."),
              ev('Third Republic proclaimed', 'event', 2.35, 48.86, 1870, None,
                 "A Government of National Defence in Paris vowed to fight on.")]),
        step(1871, 'Sep 1870 to May 1871', 'Siege of Paris and the German Empire',
             "German armies surrounded Paris from 19 September and starved it through the winter, and Bazaine surrendered "
             "Metz in October. Léon Gambetta escaped Paris by balloon and raised new armies on the Loire and in the "
             "north, but they could not break through. On 18 January 1871 Wilhelm I was proclaimed German Emperor in the "
             "Hall of Mirrors at Versailles, Paris capitulated ten days later, and the Treaty of Frankfurt gave Alsace and "
             "much of Lorraine to the new German Empire.",
             terr((0, GERMANY70), (1, ['France'])),
             [fr('Siege of Paris', PARIS_RING),
              fr('Loire front, Dec 1870', [[0.2, 48.0], [1.2, 47.85], [1.9, 47.85], [2.7, 47.95]])],
             [mv(0, 'Crown Prince Friedrich Wilhelm', 'March on Paris', [[4.94, 49.7], [4.03, 49.26], [3.4, 49.05], [2.62, 48.86]]),
              mv(0, 'Prince Friedrich Karl', 'Second Army from Metz to the Loire', [[6.18, 49.12], [4.6, 48.6], [3.28, 48.2], [1.9, 47.9], [0.2, 48.0]]),
              mv(1, 'Antoine Chanzy', 'Army of the Loire', [[0.69, 47.39], [1.66, 47.93], [1.9, 47.9]]),
              mv(1, 'Léon Gambetta', 'Escapes Paris by balloon', [[2.35, 48.86], [2.55, 49.4], [0.69, 47.39]])],
             [ev('Siege of Paris', 'siege', 2.35, 48.86, 1871, 0,
                 "After four months of hunger and shelling, Paris capitulated on 28 January."),
              ev('Proclamation of the German Empire', 'event', 2.12, 48.8, 1871, 0,
                 "The German princes hailed Wilhelm I as emperor in the palace of Versailles."),
              ev('Treaty of Frankfurt', 'treaty', 8.68, 50.11, 1871, 0,
                 "France ceded Alsace and northern Lorraine and paid an indemnity of five billion francs.")]),
    ]))

# ---------------------------------------------------------------- 4. American Civil War
US = ['United States']
WARS.append(war(
    'american-civil-war', 'American Civil War', 1861, 1865, 'war',
    "Eleven Southern slave states seceded after Abraham Lincoln's election and formed the Confederacy, which fought the "
    "United States government (the Union). After four years and some 620,000 or more military deaths, the Union's greater "
    "industry and manpower, a naval blockade and the generalship of Grant and Sherman prevailed. The war preserved the "
    "United States and ended slavery through the Thirteenth Amendment.",
    [side('Union', BLUE, ['Abraham Lincoln', 'Ulysses S. Grant', 'William T. Sherman', 'George McClellan', 'George Meade']),
     side('Confederacy', RED, ['Jefferson Davis', 'Robert E. Lee', 'Stonewall Jackson', 'Joseph E. Johnston', 'Braxton Bragg'])],
    [th(-77.5, 38.0, 4), th(-86.0, 34.0, 6.5)],
    [
        step(1861, 'Apr to Jul 1861', 'Fort Sumter and First Bull Run',
             "Confederate batteries bombarded Fort Sumter in Charleston harbour, and Lincoln called for volunteers, "
             "prompting four more states to secede while the border states of Kentucky, Missouri and Maryland were held "
             "for the Union. The first major battle, at Bull Run near Manassas, ended in a Union rout and showed the war "
             "would be long.",
             terr((0, US)),
             [fr('Union and Confederate line, 1861', [[-76.3, 37.9], [-77.2, 38.7], [-78.5, 38.9], [-80.5, 38.0], [-82.6, 37.6],
                                                     [-85.0, 36.7], [-89.2, 36.8], [-91.5, 36.5], [-94.6, 36.5]])],
             [mv(0, 'Irvin McDowell', 'Army from Washington', [[-77.04, 38.9], [-77.43, 38.84], [-77.52, 38.81]]),
              mv(1, 'Joseph E. Johnston', 'By rail from the Shenandoah', [[-78.16, 39.18], [-77.95, 39.0], [-77.55, 38.8]]),
              mv(1, 'P. G. T. Beauregard', 'Confederate army at Manassas', [[-77.47, 38.75], [-77.5, 38.78], [-77.53, 38.8]])],
             [ev('Fort Sumter', 'siege', -79.87, 32.75, 1861, 1,
                 "The Union garrison surrendered after a 34-hour bombardment, starting the war."),
              ev('First Battle of Bull Run', 'battle', -77.52, 38.81, 1861, 1,
                 "Confederate reinforcements arrived by rail and turned the battle into a Union rout.")]),
        step(1862, 'Feb to Apr 1862', 'War in the West',
             "Ulysses S. Grant captured Forts Henry and Donelson, opening Tennessee to Union armies, and survived a "
             "Confederate surprise attack at Shiloh. A Union fleet under David Farragut ran past the forts below New "
             "Orleans and took the South's largest city.",
             terr((0, US)),
             [fr('Front, spring 1862', [[-76.3, 37.9], [-77.4, 38.6], [-78.5, 38.6], [-80.5, 37.8], [-83.0, 36.9], [-85.5, 35.6],
                                        [-88.3, 35.0], [-89.6, 35.3], [-90.6, 35.5], [-94.5, 36.0]])],
             [mv(0, 'Ulysses S. Grant', 'Forts Henry and Donelson', [[-89.18, 37.0], [-88.6, 37.08], [-88.05, 36.5], [-87.86, 36.49]]),
              mv(0, 'Ulysses S. Grant', 'Up the Tennessee River', [[-88.05, 36.5], [-88.25, 35.22], [-88.33, 35.15]]),
              mv(1, 'Albert Sidney Johnston', 'Attack from Corinth', [[-88.52, 34.93], [-88.4, 35.05], [-88.33, 35.15]]),
              mv(0, 'David Farragut', 'Fleet up the Mississippi', [[-89.0, 28.6], [-89.25, 29.15], [-89.45, 29.36], [-90.06, 29.95]])],
             [ev('Battle of Fort Donelson', 'siege', -87.86, 36.49, 1862, 0,
                 "Grant forced the surrender of over 12,000 Confederates and earned the name Unconditional Surrender Grant."),
              ev('Battle of Shiloh', 'battle', -88.33, 35.15, 1862, 0,
                 "Grant's army survived a surprise attack and drove the Confederates back in a battle of shocking losses."),
              ev('Capture of New Orleans', 'siege', -90.07, 29.95, 1862, 0,
                 "Farragut's fleet captured New Orleans and closed the mouth of the Mississippi.")]),
        step(1862, 'Jun to Sep 1862', 'Lee takes command, Antietam',
             "McClellan's army landed on the Virginia peninsula and neared Richmond, but Robert E. Lee drove it back in "
             "the Seven Days Battles and then beat another Union army at Second Bull Run. Lee invaded Maryland and was "
             "checked at Antietam, the bloodiest single day in American history, after which Lincoln issued the "
             "Emancipation Proclamation.",
             terr((0, US)),
             [fr('Front, summer 1862', [[-76.3, 37.6], [-77.2, 38.4], [-78.0, 39.2], [-80.0, 38.3], [-82.5, 37.4], [-85.0, 35.8],
                                        [-88.4, 34.9], [-90.1, 35.1], [-91.5, 35.0], [-94.5, 35.6]])],
             [mv(0, 'George McClellan', 'By sea to Fort Monroe', [[-77.05, 38.8], [-77.0, 38.4], [-76.3, 38.05], [-76.2, 37.6], [-76.31, 37.02]]),
              mv(0, 'George McClellan', 'Peninsula Campaign', [[-76.31, 37.02], [-76.7, 37.27], [-77.25, 37.52]]),
              mv(1, 'Robert E. Lee', 'North into Maryland', [[-77.45, 37.55], [-77.99, 38.47], [-77.55, 38.82], [-77.56, 39.12], [-77.75, 39.45]])],
             [ev('Seven Days Battles', 'battle', -77.3, 37.5, 1862, 1,
                 "Lee's attacks drove McClellan's army away from Richmond."),
              ev('Second Battle of Bull Run', 'battle', -77.55, 38.82, 1862, 1,
                 "Lee and Jackson routed John Pope's army."),
              ev('Battle of Antietam', 'battle', -77.74, 39.47, 1862, 0,
                 "A tactically indecisive but strategic Union victory that ended Lee's first invasion of the North.")]),
        step(1863, 'May to Jul 1863', 'Gettysburg and Vicksburg',
             "Lee won his greatest victory at Chancellorsville and invaded Pennsylvania, but was defeated at Gettysburg in "
             "three days of fighting. A day later Vicksburg surrendered to Grant after a brilliant campaign and siege, "
             "giving the Union control of the Mississippi and splitting the Confederacy in two.",
             terr((0, US)),
             [fr('Eastern and central front', [[-76.3, 37.6], [-77.46, 38.3], [-78.3, 38.7], [-80.3, 38.0], [-82.5, 37.0], [-84.5, 35.7],
                                               [-86.4, 35.6], [-88.3, 34.9]]),
              fr('Union-held Mississippi', [[-90.0, 35.0], [-90.88, 32.35], [-91.2, 31.0], [-91.6, 30.5]])],
             [mv(1, 'Robert E. Lee', 'Invasion of Pennsylvania', [[-77.46, 38.3], [-78.19, 38.92], [-77.72, 39.64], [-77.23, 39.81]]),
              mv(0, 'George Meade', 'Army of the Potomac follows', [[-77.46, 38.6], [-77.2, 39.1], [-77.15, 39.6], [-77.23, 39.8]]),
              mv(0, 'Ulysses S. Grant', 'Vicksburg Campaign', [[-91.05, 32.45], [-91.2, 32.0], [-90.42, 32.26], [-90.18, 32.3], [-90.88, 32.35]])],
             [ev('Battle of Chancellorsville', 'battle', -77.63, 38.31, 1863, 1,
                 "Lee split his smaller army and routed Hooker, but Stonewall Jackson was mortally wounded."),
              ev('Battle of Gettysburg', 'battle', -77.23, 39.81, 1863, 0,
                 "Meade's army repelled Lee's assaults, including Pickett's Charge, ending his invasion."),
              ev('Siege of Vicksburg', 'siege', -90.88, 32.35, 1863, 0,
                 "Pemberton surrendered the fortress city and nearly 30,000 men on 4 July.")]),
        step(1863, 'Sep to Nov 1863', 'Chickamauga and Chattanooga',
             "Rosecrans manoeuvred the Confederates out of Chattanooga, but Bragg, reinforced by Longstreet's corps sent "
             "by rail from Virginia, routed him at Chickamauga. Grant took command, broke the siege of Chattanooga at "
             "Missionary Ridge and opened the gateway to Georgia.",
             terr((0, US)),
             [fr('Front, autumn 1863', [[-76.3, 37.6], [-77.9, 38.4], [-80.3, 37.8], [-83.0, 36.5], [-85.3, 35.0], [-86.6, 34.7],
                                        [-88.5, 34.5], [-90.2, 33.5]]),
              fr('Union-held Mississippi', [[-90.0, 35.0], [-90.88, 32.35], [-91.2, 31.0], [-91.6, 30.5]])],
             [mv(0, 'William Rosecrans', 'Advance on Chattanooga', [[-86.39, 35.85], [-86.21, 35.36], [-85.31, 35.05]]),
              mv(1, 'James Longstreet', 'Corps sent by rail', [[-77.44, 37.54], [-77.94, 34.23], [-81.97, 33.47], [-84.39, 33.75], [-85.2, 34.9]]),
              mv(0, 'Ulysses S. Grant', 'Takes command at Chattanooga', [[-86.78, 36.16], [-85.9, 35.3], [-85.31, 35.05]])],
             [ev('Battle of Chickamauga', 'battle', -85.26, 34.92, 1863, 1,
                 "The largest Confederate victory in the West drove Rosecrans back into Chattanooga."),
              ev('Battle of Chattanooga', 'battle', -85.26, 35.03, 1863, 0,
                 "Union troops stormed Missionary Ridge and routed Bragg's army.")]),
        step(1864, 'May to Jun 1864', 'The Overland Campaign',
             "Grant, now commanding all Union armies, attacked Lee relentlessly in Virginia, suffering huge losses at the "
             "Wilderness, Spotsylvania and Cold Harbor but never retreating. He swung south of Richmond and pinned Lee in "
             "a long siege at Petersburg, while Sherman began his advance from Chattanooga towards Atlanta.",
             terr((0, US)),
             [fr('Richmond and Petersburg lines', [[-77.2, 37.75], [-77.33, 37.5], [-77.4, 37.2]]),
              fr('Front in Georgia', [[-83.8, 34.6], [-84.7, 34.3], [-85.6, 34.0], [-87.5, 34.6], [-90.2, 33.5]])],
             [mv(0, 'Ulysses S. Grant', 'Overland Campaign', [[-77.8, 38.42], [-77.73, 38.31], [-77.59, 38.2], [-77.28, 37.59], [-77.4, 37.23]]),
              mv(1, 'Robert E. Lee', 'Army of Northern Virginia falls back', [[-77.75, 38.3], [-77.6, 38.18], [-77.35, 37.65], [-77.4, 37.25]]),
              mv(0, 'William T. Sherman', 'Advance on Atlanta begins', [[-85.31, 35.05], [-84.97, 34.77], [-84.6, 34.3]])],
             [ev('Battle of the Wilderness', 'battle', -77.73, 38.31, 1864, None,
                 "Two days of fighting in dense, burning woods ended without a decision, but Grant pressed on."),
              ev('Battle of Cold Harbor', 'battle', -77.28, 37.59, 1864, 1,
                 "A failed Union frontal assault cost thousands of men in a few hours."),
              ev('Siege of Petersburg begins', 'siege', -77.4, 37.23, 1864, None,
                 "Nine months of trench warfare pinned Lee's army to Richmond.")]),
        step(1864, 'Sep to Dec 1864', 'Atlanta and the March to the Sea',
             "Sherman captured Atlanta in September, helping secure Lincoln's re-election. He then cut loose from his "
             "supply lines and marched to Savannah, destroying railways and property, while Union forces under Thomas "
             "destroyed Hood's army at Franklin and Nashville.",
             terr((0, US)),
             [fr('Richmond and Petersburg lines', [[-77.2, 37.75], [-77.33, 37.5], [-77.4, 37.2]])],
             [mv(0, 'William T. Sherman', 'Atlanta Campaign', [[-85.31, 35.05], [-84.97, 34.77], [-84.6, 33.98], [-84.39, 33.75]]),
              mv(0, 'William T. Sherman', 'March to the Sea', [[-84.39, 33.75], [-83.23, 33.08], [-81.95, 32.8], [-81.09, 32.08]]),
              mv(1, 'John Bell Hood', 'Invasion of Tennessee', [[-84.39, 33.75], [-85.16, 34.26], [-87.67, 34.73], [-86.87, 35.92], [-86.78, 36.16]]),
              mv(0, 'George H. Thomas', 'Defence of Nashville', [[-85.31, 35.05], [-86.3, 35.7], [-86.78, 36.16]])],
             [ev('Fall of Atlanta', 'siege', -84.39, 33.75, 1864, 0,
                 "Sherman cut Atlanta's last railroad and Hood evacuated the city."),
              ev('Battle of Nashville', 'battle', -86.78, 36.16, 1864, 0,
                 "Thomas shattered Hood's Army of Tennessee."),
              ev('Capture of Savannah', 'siege', -81.09, 32.08, 1864, 0,
                 "Sherman reached the sea and took Savannah just before Christmas.")]),
        step(1865, 'Feb to Apr 1865', 'Appomattox',
             "Sherman marched north through the Carolinas while Grant broke Lee's lines at Five Forks, forcing the "
             "evacuation of Petersburg and Richmond. Lee's starving army was cut off and surrendered at Appomattox Court "
             "House on 9 April; Lincoln was assassinated five days later and the remaining Confederate armies soon "
             "surrendered.",
             terr((0, US)), [],
             [mv(1, 'Robert E. Lee', 'Retreat west', [[-77.4, 37.23], [-77.98, 37.34], [-78.39, 37.3], [-78.8, 37.38]]),
              mv(0, 'Ulysses S. Grant', 'Pursuit', [[-77.62, 37.14], [-78.2, 37.19], [-78.8, 37.36]]),
              mv(0, 'William T. Sherman', 'Through the Carolinas', [[-81.09, 32.08], [-81.03, 34.0], [-78.64, 35.78], [-78.95, 36.0]])],
             [ev('Battle of Five Forks', 'battle', -77.62, 37.14, 1865, 0,
                 "Sheridan's victory broke Lee's line and doomed Petersburg."),
              ev('Surrender at Appomattox Court House', 'treaty', -78.8, 37.38, 1865, 0,
                 "Lee surrendered the Army of Northern Virginia to Grant.")]),
    ]))

# ---------------------------------------------------------------- 5. Reform War
NORTH_FRONT = [[-104.5, 21.6], [-102.6, 22.6], [-100.9, 22.3], [-99.0, 21.4]]
VERA_FRONT = [[-96.75, 19.75], [-97.05, 19.1], [-96.75, 18.55]]
WARS.append(war(
    'reform-war', 'Reform War', 1857, 1861, 'war',
    "Mexico's Reform War was a civil war between Liberals, who defended the 1857 Constitution that stripped the Catholic "
    "Church and the army of their privileges, and Conservatives, who backed the Church and the old order. The Conservatives "
    "held Mexico City and won most early battles under the young general Miguel Miramón, but Benito Juárez's Liberal "
    "government held out in Veracruz on its customs revenue, issued the radical Reform Laws and won decisively at "
    "Calpulalpan in December 1860. The war left Mexico bankrupt, and Juárez's suspension of foreign debt payments in 1861 "
    "opened the way to the French intervention.",
    [side('Liberals (Juárez government)', BLUE, ['Benito Juárez', 'Santos Degollado', 'Jesús González Ortega', 'Ignacio Zaragoza', 'Santiago Vidaurri']),
     side('Conservatives', RED, ['Félix Zuloaga', 'Miguel Miramón', 'Luis Osollo', 'Leonardo Márquez', 'Tomás Mejía'])],
    [th(-100.5, 20.8, 4.5), th(-96.4, 19.1, 1.5)],
    [
        step(1858, 'Dec 1857 to Mar 1858', 'The Plan of Tacubaya',
             "President Ignacio Comonfort backed the Conservative Plan of Tacubaya in December 1857 and shut down "
             "Congress, then lost control, and in January 1858 General Félix Zuloaga took Mexico City for the "
             "Conservatives. Benito Juárez, head of the Supreme Court and so the constitutional successor, set up a "
             "Liberal government in Guanajuato and then Guadalajara. Luis Osollo routed the Liberal army at Salamanca in "
             "March, and Juárez, nearly shot by mutineers in Guadalajara, escaped to the Pacific coast.",
             [], [],
             [mv(0, 'Benito Juárez', "Juárez's flight", [[-99.13, 19.43], [-101.25, 21.02], [-103.35, 20.67], [-104.32, 19.05]]),
              mv(1, 'Luis Osollo', 'Conservative army into the Bajío', [[-99.13, 19.43], [-100.39, 20.59], [-101.19, 20.57]]),
              mv(0, 'Anastasio Parrodi', 'Liberal coalition army', [[-103.35, 20.67], [-102.2, 20.6], [-101.19, 20.57]])],
             [ev('Plan of Tacubaya', 'event', -99.19, 19.4, 1857, 1,
                 "A Conservative coup against the 1857 Constitution started the civil war."),
              ev('Battle of Salamanca', 'battle', -101.19, 20.57, 1858, 1,
                 "Osollo broke the main Liberal army in the Bajío.")]),
        step(1858, 'Apr to Dec 1858', 'Juárez in Veracruz',
             "Juárez sailed from Manzanillo by way of Panama, Havana and New Orleans and reached Veracruz in May 1858, "
             "where the port's customs duties kept his government alive. Conservative armies, led after Osollo's death "
             "by the 26-year-old Miguel Miramón, held the central plateau and beat Santiago Vidaurri's northern Liberals "
             "at Ahualulco in September, while Santos Degollado kept Liberal resistance going in the west.",
             [],
             [fr('Northern front, late 1858', NORTH_FRONT), fr('Veracruz coast held by the Liberals', VERA_FRONT)],
             [mv(0, 'Benito Juárez', 'By sea to Veracruz', [[-104.32, 19.05], [-90.0, 11.0], [-79.52, 8.97], [-82.36, 23.13], [-90.07, 29.95], [-96.13, 19.19]]),
              mv(1, 'Miguel Miramón', 'Campaign in the north', [[-99.13, 19.43], [-100.39, 20.59], [-100.98, 22.15], [-101.17, 22.4]]),
              mv(0, 'Santiago Vidaurri', 'Northern Liberals', [[-100.31, 25.67], [-100.6, 23.8], [-101.17, 22.4]])],
             [ev('Juárez reaches Veracruz', 'event', -96.13, 19.19, 1858, 0,
                 "The fortified port became the Liberal capital for the rest of the war."),
              ev('Battle of Ahualulco', 'battle', -101.17, 22.4, 1858, 1,
                 "Miramón routed Vidaurri's northern army.")]),
        step(1859, '1859', 'Siege of Veracruz and the Reform Laws',
             "Miramón, now Conservative president, marched on Veracruz in early 1859 but could not take its fortified "
             "port and fell back. Degollado struck at Mexico City and was crushed at Tacubaya in April by Leonardo "
             "Márquez, whose shooting of prisoners and medical staff earned him the name Tiger of Tacubaya. In July Juárez "
             "answered with the Reform Laws, nationalising Church property and separating Church and state.",
             [],
             [fr('Northern front', NORTH_FRONT), fr('Veracruz coast held by the Liberals', VERA_FRONT)],
             [mv(1, 'Miguel Miramón', 'March on Veracruz', [[-99.13, 19.43], [-98.2, 19.04], [-97.1, 18.85], [-96.25, 19.12]]),
              mv(0, 'Santos Degollado', 'Attack on Mexico City', [[-101.19, 19.7], [-100.0, 19.5], [-99.19, 19.4]]),
              mv(1, 'Leonardo Márquez', 'Relief of the capital', [[-103.35, 20.67], [-101.2, 20.5], [-99.19, 19.4]])],
             [ev('First siege of Veracruz', 'siege', -96.2, 19.15, 1859, 0,
                 "Miramón's army failed to breach the port's defences and withdrew."),
              ev('Battle of Tacubaya', 'battle', -99.19, 19.4, 1859, 1,
                 "Márquez routed Degollado and executed prisoners afterwards."),
              ev('Reform Laws', 'event', -96.14, 19.2, 1859, 0,
                 "Juárez's decrees nationalised Church property and created civil marriage and registry.")]),
        step(1860, 'Mar to Nov 1860', 'The tide turns',
             "In March 1860 Miramón tried again at Veracruz, but a US Navy squadron seized his small fleet from Havana at "
             "Antón Lizardo, and the second siege failed. Liberal armies of the interior under Jesús González Ortega and "
             "Ignacio Zaragoza beat Miramón at Silao in August and took Guadalajara in November, leaving the "
             "Conservatives only the area around the capital.",
             [],
             [fr('Conservative perimeter, Nov 1860', [[-101.0, 21.2], [-100.0, 20.4], [-99.0, 20.6], [-98.0, 19.8], [-97.6, 18.9]])],
             [mv(1, 'Tomás Marín', 'Conservative ships from Havana', [[-82.36, 23.13], [-90.0, 22.0], [-95.98, 19.06]]),
              mv(1, 'Miguel Miramón', 'Second march on Veracruz', [[-99.13, 19.43], [-97.1, 18.85], [-96.25, 19.12]]),
              mv(0, 'Jesús González Ortega', 'Army of the interior', [[-102.57, 22.77], [-101.68, 21.12], [-101.43, 20.94]]),
              mv(0, 'Ignacio Zaragoza', 'On to Guadalajara', [[-101.43, 20.94], [-102.5, 20.8], [-103.35, 20.67]])],
             [ev('Battle of Antón Lizardo', 'battle', -95.98, 19.06, 1860, 0,
                 "US warships captured the Conservative ships meant to blockade Veracruz."),
              ev('Battle of Silao', 'battle', -101.43, 20.94, 1860, 0,
                 "González Ortega and Zaragoza beat Miramón, the first great Liberal victory."),
              ev('Capture of Guadalajara', 'siege', -103.35, 20.67, 1860, 0,
                 "The Liberals took Mexico's second city after a long siege.")]),
        step(1861, 'Dec 1860 to Jan 1861', 'Calpulalpan and the return of Juárez',
             "González Ortega's army met Miramón's last field army at Calpulalpan on 22 December 1860 and destroyed it. "
             "Miramón fled abroad, Liberal troops entered Mexico City on Christmas Day and Juárez returned in January "
             "1861. Conservative guerrillas under Márquez and Mejía fought on, and Mexico's empty treasury soon invited "
             "European intervention.",
             terr((0, ['Viceroyalty of New Spain'])), [],
             [mv(1, 'Miguel Miramón', 'Last Conservative army', [[-99.13, 19.43], [-99.4, 19.7], [-99.6, 19.97]]),
              mv(0, 'Jesús González Ortega', 'March on the capital', [[-101.43, 20.94], [-100.39, 20.59], [-99.6, 19.97], [-99.13, 19.43]]),
              mv(0, 'Benito Juárez', 'Return to Mexico City', [[-96.13, 19.19], [-97.1, 18.85], [-98.2, 19.04], [-99.13, 19.43]])],
             [ev('Battle of Calpulalpan', 'battle', -99.6, 19.97, 1860, 0,
                 "The decisive Liberal victory that ended the war."),
              ev('Juárez returns to Mexico City', 'event', -99.13, 19.43, 1861, 0,
                 "The constitutional government was restored in the capital on 11 January 1861.")]),
    ]))

# ---------------------------------------------------------------- 6. French conquest of Vietnam
WARS.append(war(
    'french-conquest-vietnam', 'French conquest of Vietnam', 1858, 1885, 'war',
    "Between 1858 and 1885 France conquered Vietnam in stages, beginning with a naval expedition sent to protect Catholic "
    "missionaries and win a foothold in East Asia. It annexed the south as the colony of Cochinchina, made Cambodia a "
    "protectorate, and then fought the Vietnamese court, the Black Flag irregulars and finally Qing China for the north. "
    "By 1885 all of Vietnam was under French rule, the core of the French Indochina formed in 1887, although armed "
    "resistance went on for years.",
    [side('France', BLUE, ['Charles Rigault de Genouilly', 'Léonard Charner', 'Francis Garnier', 'Henri Rivière', 'Amédée Courbet']),
     side('Vietnam and its allies', RED, ['Emperor Tu Duc', 'Nguyen Tri Phuong', 'Liu Yongfu (Black Flags)', 'Ton That Thuyet', 'Qing armies in Tonkin'])],
    [th(106.5, 16.0, 6.5), th(119.4, 26.0, 1.5)],
    [
        step(1858, 'Sep 1858 to 1859', 'Landing at Tourane',
             "Citing the persecution of Catholic missionaries, Admiral Rigault de Genouilly led a Franco-Spanish fleet "
             "into the bay of Tourane (Da Nang) in September 1858 and took its forts. He hoped to march on the capital "
             "Hue, but Nguyen Tri Phuong's troops hemmed in the landing and disease ravaged the expedition.",
             terr((1, ['Annam', 'Cochin China'])),
             [fr('Tourane perimeter', [[108.1, 16.12], [108.14, 16.0], [108.25, 15.97]])],
             [mv(0, 'Rigault de Genouilly', 'Franco-Spanish fleet', [[113.5, 20.0], [110.5, 17.5], [108.25, 16.1]]),
              mv(1, 'Nguyen Tri Phuong', 'Vietnamese army from Hue', [[107.58, 16.46], [107.95, 16.25], [108.12, 16.06]])],
             [ev('Siege of Tourane', 'siege', 108.22, 16.07, 1858, 1,
                 "The French held the bay but could not break out, and finally abandoned it in 1860.")]),
        step(1861, 'Feb 1859 to Jun 1862', 'Saigon and the first treaty',
             "Rigault sailed south and captured the citadel of Saigon in February 1859, a rich rice port far from Hue. "
             "In February 1861 Admiral Charner broke the Vietnamese siege lines at Ky Hoa, and the French overran the "
             "surrounding provinces. Facing a rebellion in the north, Emperor Tu Duc signed the Treaty of Saigon in June "
             "1862, ceding three southern provinces and paying an indemnity.",
             terr((1, ['Annam', 'Cochin China'])),
             [fr('Ky Hoa lines, 1861', [[106.62, 10.83], [106.66, 10.79], [106.69, 10.76]])],
             [mv(0, 'Rigault de Genouilly', 'Fleet to Saigon', [[108.22, 16.07], [109.3, 13.5], [108.0, 10.6], [106.85, 10.4], [106.7, 10.78]]),
              mv(0, 'Léonard Charner', 'Breakout from Saigon', [[106.7, 10.78], [106.66, 10.8], [106.5, 10.55], [106.36, 10.36]]),
              mv(1, 'Nguyen Tri Phuong', 'Siege army at Ky Hoa', [[107.0, 10.95], [106.8, 10.88], [106.66, 10.81]])],
             [ev('Capture of Saigon', 'siege', 106.7, 10.78, 1859, 0,
                 "French and Spanish troops stormed the citadel of Saigon."),
              ev('Battle of Ky Hoa', 'battle', 106.66, 10.8, 1861, 0,
                 "Charner's reinforced army broke the Vietnamese lines around Saigon."),
              ev('Treaty of Saigon', 'treaty', 106.7, 10.76, 1862, 0,
                 "Vietnam ceded Bien Hoa, Gia Dinh and Dinh Tuong provinces to France.")]),
        step(1867, '1863 to 1867', 'Cochinchina and Cambodia',
             "In 1863 King Norodom of Cambodia, squeezed between Siam and Vietnam, accepted a French protectorate. In June "
             "1867 Admiral de La Grandière seized the three western provinces of the Mekong delta without a fight, and "
             "their governor Phan Thanh Gian took poison. All of the south was now the French colony of Cochinchina, and "
             "a French expedition was exploring the Mekong as a trade route to China.",
             terr((0, ['Cochin China', 'Cambodia']), (1, ['Annam'])), [],
             [mv(0, 'Pierre de La Grandière', 'Seizure of the western provinces', [[106.7, 10.78], [105.97, 10.25], [105.12, 10.7], [104.48, 10.38]]),
              mv(0, 'Doudart de Lagrée', 'Mekong expedition', [[104.92, 11.56], [105.8, 15.1], [102.6, 17.97], [102.14, 19.89], [100.8, 22.0]])],
             [ev('Cambodian protectorate', 'treaty', 104.75, 11.8, 1863, 0,
                 "King Norodom placed Cambodia under French protection at Oudong."),
              ev('Annexation of western Cochinchina', 'event', 105.97, 10.25, 1867, 0,
                 "France took Vinh Long, An Giang and Ha Tien, completing the colony.")]),
        step(1873, 'Nov 1873 to 1874', 'Garnier in Tonkin',
             "The explorer Francis Garnier was sent north in 1873 to settle a quarrel over trade on the Red River, but "
             "with a few hundred men he stormed the citadel of Hanoi and seized the delta towns. In December Liu Yongfu's "
             "Black Flags, Chinese irregulars working for the Vietnamese court, ambushed and killed him outside Hanoi. "
             "France disowned the venture and withdrew, but the 1874 treaty opened the Red River to trade.",
             terr((0, ['Cochin China', 'Cambodia']), (1, ['Annam'])), [],
             [mv(0, 'Francis Garnier', 'Expedition to Hanoi', [[106.7, 10.78], [109.3, 12.3], [108.9, 15.5], [107.0, 19.8], [106.68, 20.86], [105.85, 21.03]]),
              mv(1, 'Liu Yongfu', 'Black Flags from Son Tay', [[105.5, 21.14], [105.7, 21.07], [105.8, 21.03]])],
             [ev('Capture of the Hanoi citadel', 'siege', 105.84, 21.035, 1873, 0,
                 "Garnier's small force stormed the citadel in an hour."),
              ev('Battle of Cau Giay', 'battle', 105.8, 21.03, 1873, 1,
                 "The Black Flags ambushed and killed Garnier at the Paper Bridge."),
              ev('Treaty of 1874', 'treaty', 106.7, 10.78, 1874, None,
                 "France gave back the delta towns but gained trade rights on the Red River.")]),
        step(1883, 'Apr 1882 to Aug 1883', 'Rivière and the protectorate',
             "Commander Henri Rivière took the Hanoi citadel again in April 1882, and in May 1883 he too was killed by the "
             "Black Flags near the Paper Bridge. France now sent real forces: in August Admiral Courbet bombarded the "
             "Thuan An forts guarding Hue, and with Tu Duc just dead the court signed the Harmand Treaty, accepting a "
             "French protectorate over Annam and Tonkin.",
             terr((0, ['French Indochina']), (1, ['Annam'])),
             [fr('Hanoi front, 1883', [[105.75, 21.25], [105.74, 21.05], [105.8, 20.85]])],
             [mv(0, 'Henri Rivière', 'Up the Red River to Hanoi', [[106.68, 20.86], [106.2, 20.95], [105.85, 21.03]]),
              mv(0, 'Amédée Courbet', 'Fleet to Hue', [[107.2, 18.9], [107.9, 17.2], [107.65, 16.57]]),
              mv(1, 'Liu Yongfu', 'Black Flags attack', [[105.5, 21.14], [105.7, 21.07], [105.8, 21.04]])],
             [ev('Second Battle of Cau Giay', 'battle', 105.8, 21.03, 1883, 1,
                 "The Black Flags routed a French sortie and killed Rivière."),
              ev('Battle of Thuan An', 'battle', 107.65, 16.56, 1883, 0,
                 "Courbet's ships and landing parties took the forts at the mouth of the Hue River."),
              ev('Harmand Treaty', 'treaty', 107.58, 16.46, 1883, 0,
                 "The Hue court accepted a French protectorate over all of Vietnam.")]),
        step(1884, 'Dec 1883 to Apr 1885', 'Sino-French War',
             "Qing China, which treated Vietnam as a tributary, sent armies into Tonkin alongside the Black Flags. The "
             "French took Son Tay in December 1883 and Bac Ninh in March 1884, and when talks broke down Courbet destroyed "
             "the Chinese Fujian fleet at Fuzhou. A French push took Lang Son in February 1885, but a Chinese victory at "
             "Bang Bo forced a hasty retreat that brought down Jules Ferry's government in Paris.",
             terr((0, ['French Indochina', 'Annam']), (1, ['Manchu Empire'])),
             [fr('Tonkin front, early 1885', [[104.9, 21.4], [105.2, 21.8], [105.9, 21.75], [106.75, 21.7], [107.3, 21.5]])],
             [mv(0, 'Amédée Courbet', 'Attack on Son Tay', [[105.85, 21.03], [105.65, 21.1], [105.5, 21.14]]),
              mv(0, "Louis Brière de l'Isle", 'Lang Son campaign', [[106.07, 21.18], [106.3, 21.45], [106.76, 21.85]]),
              mv(1, 'Feng Zicai', 'Guangxi Army counterattack', [[106.73, 22.15], [106.74, 22.0], [106.6, 21.7]]),
              mv(0, 'Amédée Courbet', 'Far East Squadron to Fuzhou', [[121.5, 25.4], [120.2, 26.1], [119.45, 26.0]])],
             [ev('Capture of Son Tay', 'siege', 105.5, 21.14, 1883, 0,
                 "Courbet stormed the Black Flag stronghold west of Hanoi."),
              ev('Battle of Fuzhou', 'battle', 119.45, 26.0, 1884, 0,
                 "Courbet's squadron sank most of the Fujian fleet in under an hour."),
              ev('Battle of Bang Bo', 'battle', 106.74, 22.0, 1885, 1,
                 "Feng Zicai's troops threw the French back from the Chinese border.")]),
        step(1885, 'Jun to Jul 1885', 'Treaty of Tianjin and Can Vuong',
             "In June 1885 China signed the Treaty of Tianjin, gave up its claims and pulled its troops out of Tonkin. "
             "In July the regent Ton That Thuyet attacked the French garrison in Hue, failed, and fled into the mountains "
             "with the boy emperor Ham Nghi, calling on the people to rise in the Can Vuong (Aid the King) movement. The "
             "French put a new emperor on the throne and spent the next decade crushing the resistance.",
             terr((0, ['French Indochina', 'Annam'])), [],
             [mv(1, 'Ton That Thuyet', 'Flight with Emperor Ham Nghi', [[107.58, 16.46], [107.0, 16.75], [106.4, 17.5], [105.6, 18.2]]),
              mv(0, 'General de Courcy', 'French garrison in Hue', [[107.65, 16.56], [107.6, 16.5], [107.58, 16.47]])],
             [ev('Treaty of Tianjin', 'treaty', 117.2, 39.13, 1885, 0,
                 "China recognised the French protectorate over Vietnam."),
              ev('Fall of Hue', 'battle', 107.58, 16.47, 1885, 0,
                 "A night attack on the French garrison failed and the court fled the capital."),
              ev('Can Vuong edict', 'event', 106.4, 17.5, 1885, None,
                 "Issued in Ham Nghi's name, it called scholars and villagers to resist the French.")]),
    ]))

# ---------------------------------------------------------------- 7. Russian conquest of Central Asia
RU = ['Russian Empire']
WARS.append(war(
    'russian-conquest-central-asia', 'Russian conquest of Central Asia', 1839, 1881, 'conflict',
    "Over four decades the Russian Empire advanced south from the Kazakh steppe into the oasis khanates of Central Asia, "
    "driven by the search for secure frontiers, trade and cotton, and by rivalry with Britain in the Great Game. Small, "
    "well-armed columns took Tashkent in 1865 and Samarkand in 1868, made Bukhara and Khiva protectorates and annexed "
    "Kokand, and the storming of the Turkmen fortress of Geok Tepe in 1881 completed the conquest. Russian Turkestan was "
    "ruled as a colony until 1917, and its borders shaped today's Central Asian states.",
    [side('Russian Empire', BLUE, ['Vasily Perovsky', 'Mikhail Chernyaev', 'Konstantin von Kaufman', 'Mikhail Skobelev']),
     side('Central Asian khanates and Turkmen', RED, ['Alimqul of Kokand', 'Emir Muzaffar of Bukhara', 'Muhammad Rahim Khan II of Khiva', 'Khudayar Khan of Kokand', 'Akhal Teke Turkmen'])],
    [th(63.0, 43.0, 9), th(56.0, 48.5, 4)],
    [
        step(1839, '1839 to 1840', "Perovsky's winter march on Khiva",
             "To end Khivan raids and slave taking on the steppe, the governor of Orenburg, Vasily Perovsky, led about "
             "5,000 men and 10,000 camels south in November 1839. A savage winter killed most of the camels and many men "
             "before they had covered half the distance, and Perovsky turned back near the Emba in early 1840. Russia "
             "learned to advance slowly, behind lines of forts.",
             terr((0, RU), (1, ['Turan', 'central Asian khanates'])),
             [fr('Orenburg line, 1839', [[51.37, 51.23], [55.1, 51.77], [58.57, 51.2], [61.56, 54.08]])],
             [mv(0, 'Vasily Perovsky', 'Winter expedition', [[55.1, 51.77], [56.0, 49.6], [57.4, 47.6], [58.2, 47.0]]),
              mv(0, 'Vasily Perovsky', 'Retreat, spring 1840', [[58.2, 47.0], [57.0, 48.2], [55.3, 51.5]])],
             [ev('Expedition turns back', 'event', 58.2, 47.0, 1840, 1,
                 "Snow, cold and camel deaths stopped the column near the Emba, c. 1840.")]),
        step(1853, '1847 to 1854', 'Forts on the Syr Darya',
             "Russia built forts across the steppe, put steamers on the Aral Sea and in 1853 Perovsky stormed the Kokandi "
             "fortress of Ak-Mechet on the Syr Darya, renaming it Fort Perovsky. From Siberia another line of forts "
             "reached the foothills of the Tian Shan, where Fort Verny, later Almaty, was founded in 1854. Between the two "
             "lines a gap of hundreds of kilometres still led to Tashkent.",
             terr((0, RU + ['central Asian khanates']), (1, ['Turan'])),
             [fr('Syr Darya line', [[61.0, 46.0], [63.5, 45.6], [65.5, 44.85], [66.8, 44.3]]),
              fr('Siberian line', [[74.5, 43.0], [76.95, 43.25], [79.06, 45.12]])],
             [mv(0, 'Vasily Perovsky', 'Up the Syr Darya', [[55.1, 51.77], [59.0, 48.5], [61.0, 46.0], [65.5, 44.85]]),
              mv(0, 'Siberian Cossacks', 'South from Semipalatinsk', [[80.25, 50.4], [80.0, 47.5], [79.06, 45.12], [76.95, 43.25]])],
             [ev('Capture of Ak-Mechet', 'siege', 65.5, 44.85, 1853, 0,
                 "Perovsky stormed the Kokandi fort, anchoring the Syr Darya line."),
              ev('Founding of Fort Verny', 'event', 76.95, 43.25, 1854, 0,
                 "The new fort, later Almaty, held the southern end of the Siberian line.")]),
        step(1865, '1864 to 1865', 'Chernyaev takes Tashkent',
             "In 1864 columns from both lines closed the gap, taking Aulie-Ata, Turkestan and Chimkent. Colonel Mikhail "
             "Chernyaev then attacked Tashkent, the largest city of Central Asia, without clear orders; its Kokandi "
             "defender Alimqul was killed, and the city fell after street fighting in June 1865. St Petersburg accepted "
             "the conquest and made Tashkent the centre of a new Turkestan province.",
             terr((0, RU + ['central Asian khanates']), (1, ['Turan'])),
             [fr('New Kokand line, 1864', [[66.8, 44.3], [68.27, 43.3], [69.6, 42.32], [71.37, 42.9], [74.5, 43.0]])],
             [mv(0, 'Mikhail Chernyaev', 'From Verny to Tashkent', [[76.95, 43.25], [71.37, 42.9], [69.6, 42.32], [69.24, 41.3]]),
              mv(0, 'Nikolai Veryovkin', 'Up the Syr Darya', [[65.5, 44.85], [68.27, 43.3], [69.6, 42.32]]),
              mv(1, 'Alimqul', 'Kokandi army to Tashkent', [[70.94, 40.53], [70.2, 40.9], [69.3, 41.25]])],
             [ev('Capture of Chimkent', 'siege', 69.6, 42.32, 1864, 0,
                 "Chernyaev's storm of Chimkent closed the gap between the two lines."),
              ev('Capture of Tashkent', 'siege', 69.24, 41.3, 1865, 0,
                 "Chernyaev stormed the city of 100,000 with under 2,000 men.")]),
        step(1868, '1866 to 1868', 'Bukhara and Samarkand',
             "Emir Muzaffar of Bukhara demanded Tashkent back and was routed at Irjar in 1866. General Konstantin von "
             "Kaufman, first governor-general of Turkestan, marched up the Zeravshan valley and took Samarkand, "
             "Tamerlane's old capital, in May 1868, then beat the emir on the Zerabulak heights while a small garrison "
             "held Samarkand against a rising. Bukhara became a Russian protectorate, shorn of Samarkand.",
             terr((0, RU + ['central Asian khanates']), (1, ['Turan'])),
             [fr('Zeravshan front, Jun 1868', [[66.0, 40.2], [66.3, 39.8], [66.5, 39.3]])],
             [mv(0, 'Dmitry Romanovsky', 'Irjar campaign, 1866', [[69.24, 41.3], [68.9, 40.75], [68.7, 40.4]]),
              mv(0, 'Konstantin von Kaufman', 'Up the Zeravshan', [[69.24, 41.3], [67.84, 40.12], [66.96, 39.65], [66.3, 39.8]]),
              mv(1, 'Emir Muzaffar', 'Bukharan army', [[64.42, 39.77], [65.5, 39.8], [66.2, 39.8]])],
             [ev('Capture of Samarkand', 'siege', 66.96, 39.65, 1868, 0,
                 "Samarkand opened its gates to Kaufman after the Bukharan army fled."),
              ev('Battle of Zerabulak', 'battle', 66.3, 39.8, 1868, 0,
                 "Kaufman broke the emir's last army near Katta-Kurgan, c. June 1868."),
              ev('Bukhara becomes a protectorate', 'treaty', 64.42, 39.77, 1868, 0,
                 "Emir Muzaffar ceded Samarkand and accepted Russian supremacy.")]),
        step(1873, 'Feb to Aug 1873', 'The march on Khiva',
             "Kaufman sent columns converging across the deserts on Khiva from Tashkent, Orenburg and the Caspian. The "
             "column from Krasnovodsk had to turn back for lack of water, but the others met outside Khiva, which "
             "surrendered in May 1873. Khan Muhammad Rahim II signed a treaty making Khiva a Russian protectorate, "
             "freeing its slaves and ceding the right bank of the Amu Darya.",
             terr((0, RU + ['central Asian khanates']), (1, ['Turan'])), [],
             [mv(0, 'Konstantin von Kaufman', 'Turkestan column', [[69.24, 41.3], [67.84, 40.12], [64.0, 41.5], [61.4, 41.6], [60.36, 41.38]]),
              mv(0, 'Nikolai Veryovkin', 'Orenburg column', [[55.1, 51.77], [58.5, 47.0], [59.0, 44.5], [58.9, 43.07], [60.36, 41.38]]),
              mv(0, 'Nikolai Lomakin', 'Mangyshlak column', [[50.25, 44.52], [55.0, 43.5], [58.9, 43.07], [60.3, 41.45]]),
              mv(0, 'Vasily Markozov', 'Krasnovodsk column turns back', [[52.98, 40.02], [55.0, 39.5], [56.5, 39.6]])],
             [ev('Surrender of Khiva', 'siege', 60.36, 41.38, 1873, 0,
                 "The khanate's capital surrendered after a brief bombardment."),
              ev('Treaty of Gandumian', 'treaty', 60.42, 41.33, 1873, 0,
                 "Khiva became a Russian protectorate and abolished slavery.")]),
        step(1876, '1875 to 1876', 'The end of Kokand',
             "A revolt against Khudayar Khan, the Russian-backed ruler of Kokand, turned into a holy war against Russia in "
             "1875. Kaufman and the young Mikhail Skobelev beat the rebels at Makhram and stormed their strongholds in the "
             "Fergana valley. In February 1876 Russia abolished the khanate and annexed it as the province of Fergana.",
             terr((0, RU + ['central Asian khanates']), (1, ['Turan'])), [],
             [mv(0, 'Konstantin von Kaufman', 'Into the Fergana valley', [[69.24, 41.3], [69.62, 40.28], [69.95, 40.42], [70.94, 40.53]]),
              mv(0, 'Mikhail Skobelev', 'Storm of Andijan', [[70.94, 40.53], [71.8, 40.7], [72.34, 40.78]])],
             [ev('Battle of Makhram', 'battle', 69.95, 40.42, 1875, 0,
                 "Kaufman routed the main rebel army on the Syr Darya, c. August 1875."),
              ev('Storming of Andijan', 'siege', 72.34, 40.78, 1876, 0,
                 "Skobelev's capture of Andijan broke the last resistance in Fergana."),
              ev('Annexation of Kokand', 'event', 70.94, 40.53, 1876, 0,
                 "The khanate was abolished and became the Russian province of Fergana.")]),
        step(1881, '1879 to 1881', 'Geok Tepe',
             "The Akhal Teke Turkmen beat off a Russian assault on their mud-walled fortress of Geok Tepe in 1879. "
             "Skobelev returned in 1880 with a railway built across the desert from the Caspian, besieged the fortress and "
             "in January 1881 blew a breach with a mine and stormed it; thousands of defenders and civilians were killed "
             "in the assault and pursuit. The Turkmen lands were annexed as Transcaspia, and Merv submitted in 1884.",
             terr((0, RU), (1, ['Bokhara Khanate'])),
             [fr('Siege lines, Jan 1881', [[57.92, 38.18], [57.95, 38.13], [58.0, 38.14]])],
             [mv(0, 'Nikolai Lomakin', 'Repulsed, 1879', [[52.98, 40.02], [56.27, 38.98], [57.9, 38.17]]),
              mv(0, 'Mikhail Skobelev', 'Akhal Teke expedition', [[53.0, 39.9], [56.27, 38.98], [57.6, 38.3], [57.96, 38.15]]),
              mv(0, 'Aleksey Kuropatkin', 'Turkestan detachment', [[60.36, 41.38], [59.0, 39.5], [58.0, 38.17]])],
             [ev('First Battle of Geok Tepe', 'battle', 57.9, 38.18, 1879, 1,
                 "The Turkmen defeated Lomakin's assault and drove the Russians back to the Caspian."),
              ev('Siege of Geok Tepe', 'siege', 57.97, 38.15, 1881, 0,
                 "Skobelev stormed the fortress, ending Turkmen resistance.")]),
    ]))

# ---------------------------------------------------------------- 8. Paraguayan War
ALLIES = ['Viceroyalty of Brazil', 'United Provinces of the Río de la Plata']
HUMAITA = [[-58.62, -27.13], [-58.5, -27.18], [-58.38, -27.2], [-58.28, -27.17]]
WARS.append(war(
    'paraguayan-war', 'Paraguayan War', 1864, 1870, 'war',
    "The Paraguayan War, or War of the Triple Alliance, began when Paraguay's ruler Francisco Solano López, fearing Brazilian "
    "and Argentine dominance over the river states, attacked Brazil after it intervened in Uruguay, and then Argentina when "
    "it refused his army passage. Brazil, Argentina and Uruguay allied against him and, after a long, bloody struggle around "
    "the river fortress of Humaitá, occupied Asunción and hunted López down in 1870. Paraguay lost a large share of its "
    "population, by some estimates more than half, and much territory in the deadliest interstate war in Latin American history.",
    [side('Triple Alliance (Brazil, Argentina, Uruguay)', BLUE, ['Bartolomé Mitre', 'Duke of Caxias', 'Count of Eu', 'Admiral Barroso', 'Venancio Flores']),
     side('Paraguay', RED, ['Francisco Solano López', 'Antonio Estigarribia', 'José E. Díaz', 'Bernardino Caballero'])],
    [th(-58.0, -26.0, 4.5), th(-57.6, -31.0, 3.5), th(-57.7, -19.8, 1.5)],
    [
        step(1864, 'Oct 1864 to Feb 1865', 'Brazil in Uruguay, López strikes',
             "Brazil invaded Uruguay in October 1864 to back Venancio Flores's Colorado rebels against the Blanco "
             "government, Paraguay's ally, and besieged Paysandú. López answered by seizing a Brazilian steamer on the "
             "Paraguay River and sending an expedition upriver that overran Brazil's lightly held province of Mato Grosso "
             "in December. Paysandú fell in January 1865 and Flores took power in Montevideo.",
             terr((0, ['Viceroyalty of Brazil']), (1, ['Paraguay'])), [],
             [mv(0, 'Venancio Flores and Admiral Tamandaré', 'Into Uruguay', [[-57.09, -29.76], [-57.96, -31.38], [-58.08, -32.32]]),
              mv(1, 'Vicente Barrios', 'Expedition up the Paraguay River', [[-57.64, -25.28], [-57.9, -22.1], [-57.75, -19.92], [-57.65, -19.0]])],
             [ev('Siege of Paysandú', 'siege', -58.08, -32.32, 1865, 0,
                 "Brazilian and Colorado forces took the Blanco stronghold after a month's siege."),
              ev('Fall of Fort Coimbra', 'siege', -57.75, -19.92, 1864, 1,
                 "The Paraguayans forced the Brazilian fort and overran southern Mato Grosso.")]),
        step(1865, 'Apr to Sep 1865', 'Invasion of Corrientes',
             "When Argentina refused to let his army cross its territory, López invaded the Argentine province of "
             "Corrientes in April 1865, and Brazil, Argentina and Uruguay signed the Treaty of the Triple Alliance. The "
             "Brazilian navy under Admiral Barroso destroyed the Paraguayan fleet at Riachuelo in June, and a Paraguayan "
             "column under Estigarribia that pushed down the Uruguay River into Brazil was surrounded and surrendered at "
             "Uruguaiana in September.",
             terr((0, ALLIES), (1, ['Paraguay'])), [],
             [mv(1, 'Wenceslao Robles', 'Invasion of Corrientes', [[-58.57, -27.32], [-58.83, -27.47], [-59.0, -28.4], [-59.27, -29.14]]),
              mv(1, 'Antonio Estigarribia', 'Down the Uruguay River', [[-55.87, -27.33], [-55.97, -28.65], [-57.09, -29.76]]),
              mv(0, 'Admiral Barroso', 'Brazilian squadron up the Paraná', [[-58.4, -34.0], [-60.65, -32.95], [-60.5, -31.7], [-59.6, -29.2], [-58.78, -27.55]]),
              mv(0, 'Bartolomé Mitre', 'Allied army to Uruguaiana', [[-58.08, -32.32], [-57.96, -31.38], [-57.15, -29.8]])],
             [ev('Treaty of the Triple Alliance', 'treaty', -58.38, -34.6, 1865, 0,
                 "Brazil, Argentina and Uruguay agreed to fight until López was removed."),
              ev('Battle of Riachuelo', 'battle', -58.78, -27.55, 1865, 0,
                 "Barroso's squadron destroyed the Paraguayan navy, giving the allies control of the rivers."),
              ev('Siege of Uruguaiana', 'siege', -57.09, -29.76, 1865, 0,
                 "Estigarribia's column of some 5,000 men surrendered to the allies.")]),
        step(1866, 'Apr to Sep 1866', 'Tuyutí and Curupayty',
             "The allies crossed the Paraná at Paso de Patria in April 1866 and dug in at Tuyutí, where on 24 May they "
             "beat off a massive Paraguayan attack in the largest battle ever fought in South America. They then stalled "
             "before the trench lines covering the river fortress of Humaitá, and in September an allied frontal assault "
             "on Curupayty was cut to pieces, halting the advance for a year.",
             terr((0, ALLIES), (1, ['Paraguay'])),
             [fr('Humaitá lines, 1866', HUMAITA)],
             [mv(0, 'Bartolomé Mitre', 'Crossing at Paso de Patria', [[-58.75, -27.5], [-58.57, -27.32], [-58.38, -27.25]]),
              mv(1, 'José E. Díaz', 'Attack at Tuyutí', [[-58.45, -27.15], [-58.4, -27.2], [-58.37, -27.24]]),
              mv(0, 'Bartolomé Mitre', 'Assault on Curupayty', [[-58.55, -27.22], [-58.58, -27.17], [-58.6, -27.14]])],
             [ev('Battle of Tuyutí', 'battle', -58.37, -27.23, 1866, 0,
                 "Allied firepower shattered López's attack, killing or wounding some 13,000 Paraguayans."),
              ev('Battle of Curupayty', 'battle', -58.6, -27.14, 1866, 1,
                 "Díaz's entrenched defenders cut down thousands of attackers for small losses.")]),
        step(1868, '1867 to Aug 1868', 'Caxias and the fall of Humaitá',
             "The Brazilian Marshal Caxias took over the allied command, rebuilt the army and outflanked the Humaitá lines "
             "to the east. In February 1868 Brazilian ironclads forced their way upriver past the fortress, and López "
             "slipped away to new lines further north; the starving garrison of Humaitá surrendered in August.",
             terr((0, ALLIES), (1, ['Paraguay'])),
             [fr('Humaitá lines', HUMAITA)],
             [mv(0, 'Duke of Caxias', 'Flank march around Humaitá', [[-58.37, -27.23], [-58.25, -27.02], [-58.4, -26.95]]),
              mv(0, 'Delfim de Carvalho', 'Ironclads pass Humaitá', [[-58.62, -27.16], [-58.52, -27.05], [-58.3, -26.6], [-57.75, -25.85]]),
              mv(1, 'Francisco Solano López', 'Withdrawal north', [[-58.51, -27.07], [-58.2, -26.7], [-57.7, -26.0], [-57.55, -25.75]])],
             [ev('Passage of Humaitá', 'battle', -58.52, -27.05, 1868, 0,
                 "Six Brazilian ironclads ran past the fortress guns under fire."),
              ev('Fall of Humaitá', 'siege', -58.5, -27.08, 1868, 0,
                 "The cut-off garrison surrendered after its supplies ran out.")]),
        step(1868, 'Dec 1868 to Jan 1869', 'The Dezembrada and Asunción',
             "Caxias built a road through the Chaco swamps, landed his army behind López's new Piquisiry line and struck "
             "from the north in a run of December battles at Itororó, Avay and Lomas Valentinas. The Paraguayan army was "
             "nearly destroyed, though López escaped, and allied troops occupied a deserted Asunción on 1 January 1869.",
             terr((0, ALLIES), (1, ['Paraguay'])),
             [fr('Piquisiry line, Dec 1868', [[-57.57, -25.75], [-57.45, -25.66], [-57.35, -25.6]])],
             [mv(0, 'Duke of Caxias', 'Chaco road and landing', [[-58.3, -26.5], [-57.95, -25.95], [-57.65, -25.4], [-57.52, -25.53]]),
              mv(0, 'Duke of Caxias', 'Occupation of Asunción', [[-57.52, -25.53], [-57.6, -25.4], [-57.64, -25.28]]),
              mv(1, 'Francisco Solano López', 'Escape to the hills', [[-57.52, -25.55], [-57.3, -25.5], [-57.05, -25.47]])],
             [ev('Battle of Lomas Valentinas', 'battle', -57.52, -25.55, 1868, 0,
                 "A week of fighting destroyed most of the remaining Paraguayan army."),
              ev('Occupation of Asunción', 'event', -57.64, -25.28, 1869, 0,
                 "Brazilian troops entered the abandoned capital on 1 January.")]),
        step(1870, '1869 to Mar 1870', 'Cordillera campaign and Cerro Corá',
             "López raised a last army of old men and boys in the hills east of Asunción. The Count of Eu, Emperor Pedro "
             "II's son-in-law, stormed his new capital Piribebuy in August 1869 and destroyed the remnant at Acosta Ñu, "
             "where many of the Paraguayan soldiers were children. Hunted into the northern forests, López was killed by "
             "Brazilian cavalry at Cerro Corá on 1 March 1870, ending the war.",
             terr((0, ALLIES), (1, ['Paraguay'])), [],
             [mv(0, 'Count of Eu', 'Cordillera campaign', [[-57.64, -25.28], [-57.3, -25.4], [-57.05, -25.47]]),
              mv(1, 'Francisco Solano López', 'Last retreat', [[-57.05, -25.47], [-56.82, -25.24], [-56.43, -24.66], [-56.0, -23.3], [-56.03, -22.65]]),
              mv(0, 'José Antônio Correia da Câmara', 'Cavalry pursuit', [[-57.43, -23.4], [-56.6, -22.9], [-56.05, -22.66]])],
             [ev('Battle of Piribebuy', 'battle', -57.05, -25.47, 1869, 0,
                 "The Count of Eu stormed López's provisional capital."),
              ev('Battle of Acosta Ñu', 'battle', -56.97, -25.4, 1869, 0,
                 "Thousands of Paraguayans, many of them boys, died covering López's retreat."),
              ev('Battle of Cerro Corá', 'battle', -56.03, -22.65, 1870, 0,
                 "López was killed by Brazilian troops, ending the war.")]),
    ]))

# ---------------------------------------------------------------- 9. Russo-Turkish War 1877-78
RU78 = ['Russian Empire', 'Romania', 'Serbia', 'Montenegro', 'Bulgaria']
WARS.append(war(
    'russo-turkish-war-1877', 'Russo-Turkish War', 1877, 1878, 'war',
    "After Ottoman forces brutally crushed a Bulgarian uprising in 1876, Russia declared war in April 1877 to back the "
    "Balkan Christians and extend its own influence, and Romania, Serbia and Montenegro fought on its side. The Russians "
    "crossed the Danube quickly but were held for five months at Plevna before crossing the Balkan mountains in winter and "
    "reaching the outskirts of Constantinople. The Treaty of San Stefano created a large Bulgaria, but the Great Powers cut "
    "it back at the Congress of Berlin, which recognised Romania, Serbia and Montenegro as independent.",
    [side('Russia and its allies', BLUE, ['Grand Duke Nicholas', 'Iosif Gurko', 'Mikhail Skobelev', 'Eduard Totleben', 'Mikhail Loris-Melikov', 'Carol I of Romania']),
     side('Ottoman Empire', RED, ['Osman Pasha', 'Süleyman Pasha', 'Ahmed Mukhtar Pasha', 'Mehmed Ali Pasha'])],
    [th(26.0, 43.0, 4), th(42.8, 40.7, 2)],
    [
        step(1877, 'Apr to Jul 1877', 'Across the Danube',
             "Russia declared war on 24 April 1877, and its army under Grand Duke Nicholas marched through allied Romania "
             "to the Danube. On 27 June General Dragomirov's division crossed the river at Svishtov, and the army fanned "
             "out into Bulgaria while a vanguard under Gurko pushed through the Balkan passes. In the Caucasus another "
             "Russian army under Loris-Melikov took Ardahan and closed on Kars.",
             terr((0, ['Russian Empire']), (1, ['Ottoman Empire'])),
             [fr('Danube front, Jun 1877', [[22.9, 44.0], [24.0, 43.75], [25.35, 43.63], [26.5, 44.05], [27.9, 44.1]])],
             [mv(0, 'Grand Duke Nicholas', 'Through Romania to the Danube', [[28.86, 47.0], [28.25, 46.48], [27.0, 45.4], [26.1, 44.43], [25.36, 43.65]]),
              mv(0, 'Iosif Gurko', 'Advance guard over the Balkans', [[25.35, 43.62], [25.62, 43.08], [25.55, 42.77], [25.4, 42.62]]),
              mv(0, 'Mikhail Loris-Melikov', 'Caucasus army', [[43.85, 40.79], [42.7, 41.11], [43.1, 40.62]])],
             [ev('Crossing of the Danube at Svishtov', 'battle', 25.35, 43.62, 1877, 0,
                 "Dragomirov's troops crossed in boats under fire and secured a bridgehead."),
              ev('Capture of Ardahan', 'siege', 42.7, 41.11, 1877, 0,
                 "Loris-Melikov's army stormed the fortress in May.")]),
        step(1877, 'Jul to Dec 1877', 'Plevna and Shipka',
             "Osman Pasha marched from Vidin and dug in at Plevna, on the flank of the Russian advance, and threw back three "
             "Russian and Romanian assaults in July and September at a cost of tens of thousands of attackers. Süleyman "
             "Pasha's army failed to break through the Russians holding the Shipka Pass in August, and the engineer "
             "Totleben starved Plevna into submission; Osman's army tried to break out and surrendered on 10 December. "
             "In the Caucasus the Russians stormed Kars in November.",
             terr((0, ['Russian Empire']), (1, ['Ottoman Empire'])),
             [fr('Russian line, autumn 1877', [[24.62, 43.42], [24.72, 43.13], [25.32, 42.75], [25.88, 42.93], [26.3, 43.4], [25.97, 43.85]]),
              fr('Caucasus front', [[42.6, 40.9], [43.1, 40.55], [43.5, 40.2]])],
             [mv(1, 'Osman Pasha', 'From Vidin to Plevna', [[22.88, 43.99], [23.6, 43.7], [24.62, 43.42]]),
              mv(1, 'Süleyman Pasha', 'Attack on the Shipka Pass', [[26.56, 41.68], [25.63, 42.43], [25.32, 42.73]]),
              mv(0, 'Eduard Totleben and Carol I', 'Siege of Plevna', [[25.35, 43.62], [25.0, 43.5], [24.66, 43.44]]),
              mv(0, 'Mikhail Loris-Melikov', 'Storm of Kars', [[43.4, 40.4], [43.25, 40.5], [43.1, 40.6]])],
             [ev('Siege of Plevna', 'siege', 24.62, 43.42, 1877, 0,
                 "Osman Pasha surrendered with over 40,000 men after a five-month defence."),
              ev('Battle of Shipka Pass', 'battle', 25.32, 42.75, 1877, 0,
                 "Russian troops and Bulgarian volunteers held the pass against Süleyman's attacks."),
              ev('Capture of Kars', 'siege', 43.1, 40.6, 1877, 0,
                 "A night assault took the great Caucasus fortress on 18 November.")]),
        step(1878, 'Dec 1877 to Jan 1878', 'Over the Balkans in winter',
             "Freed by the fall of Plevna, the Russians crossed the snowbound Balkan mountains in midwinter. Gurko took "
             "Sofia on 4 January and beat Süleyman at Philippopolis, while Radetzky and Skobelev surrounded and captured "
             "the Ottoman army at Shipka-Sheinovo. With their field armies gone, the Ottomans lost Adrianople on 20 "
             "January and asked for an armistice.",
             terr((0, RU78), (1, ['Ottoman Empire', 'Bosnia-Herzegovina'])), [],
             [mv(0, 'Iosif Gurko', 'Winter crossing to Sofia and Philippopolis', [[23.79, 42.9], [23.32, 42.7], [24.75, 42.15], [26.56, 41.68]]),
              mv(0, 'Mikhail Skobelev', 'Through the Shipka Pass', [[25.32, 42.75], [25.38, 42.67], [25.63, 42.43], [26.5, 41.72]]),
              mv(1, 'Süleyman Pasha', 'Retreat to the Aegean', [[25.63, 42.43], [24.75, 42.15], [25.0, 41.6], [25.87, 40.85]])],
             [ev('Battle of Shipka-Sheinovo', 'battle', 25.38, 42.67, 1878, 0,
                 "Skobelev and Radetzky captured Vessel Pasha's army of some 30,000 men."),
              ev('Battle of Philippopolis', 'battle', 24.75, 42.15, 1878, 0,
                 "Gurko broke Süleyman's army in three days of fighting."),
              ev('Fall of Adrianople', 'event', 26.56, 41.68, 1878, 0,
                 "The Ottomans gave up their second city without a fight.")]),
        step(1878, 'Feb to Jul 1878', 'San Stefano and Berlin',
             "As Russian troops advanced to San Stefano, within sight of Constantinople, a British fleet entered the Sea "
             "of Marmara to warn them off. The Treaty of San Stefano on 3 March created a large Bulgaria reaching the "
             "Aegean, alarming Britain and Austria-Hungary. At the Congress of Berlin in July the powers split Bulgaria, "
             "recognised Romania, Serbia and Montenegro as independent, gave Russia Kars and Batum, let Austria-Hungary "
             "occupy Bosnia and Herzegovina, and gave Britain Cyprus.",
             terr((0, RU78), (1, ['Ottoman Empire'])),
             [fr('Russian forward line, Mar 1878', [[28.6, 41.3], [28.72, 41.08], [28.8, 40.97]])],
             [mv(0, 'Grand Duke Nicholas', 'Advance to San Stefano', [[26.56, 41.68], [27.8, 41.16], [28.82, 40.96]])],
             [ev('Treaty of San Stefano', 'treaty', 28.82, 40.96, 1878, 0,
                 "The Ottomans accepted a large autonomous Bulgaria and the independence of Romania, Serbia and Montenegro."),
              ev('Congress of Berlin', 'treaty', 13.4, 52.52, 1878, None,
                 "The Great Powers revised San Stefano, shrinking Bulgaria and limiting Russia's gains.")]),
    ]))

# ---------------------------------------------------------------- checks + write
DASH = re.compile('[–—]')


def walk(o, path=''):
    if isinstance(o, dict):
        for k, v in o.items():
            if k == 'polities':
                continue
            walk(v, path + '.' + k)
    elif isinstance(o, list):
        for i, v in enumerate(o):
            walk(v, '%s[%d]' % (path, i))
    elif isinstance(o, str) and DASH.search(o):
        raise SystemExit('dash in %s: %s' % (path, o))


walk(WARS)
for w in WARS:
    for s in w['steps']:
        assert len(s['moves']) <= 5 and len(s['events']) <= 3, (w['id'], s['title'])
out = os.path.join(H, 'wars_g10.json')
json.dump(WARS, open(out, 'w'), ensure_ascii=False, indent=1)
print('wrote', out, len(WARS), 'wars', sum(len(w['steps']) for w in WARS), 'steps')
