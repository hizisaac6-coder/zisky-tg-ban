#!/usr/bin/env python3
"""
╔══════════════════════════════════════════════════════════════════════════════╗
║                                                                              ║
║   ███████╗██╗███████╗██╗  ██╗██╗   ██╗    ████████╗ ██████╗     ██████╗ █████╗ ██╗   ██╗
║   ╚══███╔╝██║██╔════╝██║ ██╔╝██║   ██║    ╚══██╔══╝██╔═══██╗    ██╔══██╗██╔══██╗██║   ██║
║     ███╔╝ ██║███████╗█████╔╝ ██║   ██║       ██║   ██║   ██║    ██████╔╝███████║██║   ██║
║    ███╔╝  ██║╚════██║██╔═██╗ ██║   ██║       ██║   ██║   ██║    ██╔══██╗██╔══██║╚██╗ ██╔╝
║   ███████╗██║███████║██║  ██╗╚██████╔╝       ██║   ╚██████╔╝    ██║  ██║██║  ██║ ╚████╔╝ 
║   ╚══════╝╚═╝╚══════╝╚═╝  ╚═╝ ╚═════╝        ╚═╝    ╚═════╝     ╚═╝  ╚═╝╚═╝  ╚═╝  ╚═══╝  
║                                                                              ║
║                    🔥 TELEGRAM MASS REPORTING TOOL v4.0 🔥                    ║
║              📧 EMAIL: Proxies.txt • 🌐 WEB: https.txt • 🔄 DUAL FILES        ║
║                    ⚡ 50+ PROFESSIONAL REPORT MESSAGES ⚡                      ║
║                                                                              ║
╚══════════════════════════════════════════════════════════════════════════════╝
"""

import os
import sys
import json
import random
import time
import re
import threading
import requests
import smtplib
import socket
import socks
import concurrent.futures
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from datetime import datetime, timedelta
from colorama import Fore, Style, init, Back
import urllib3
import ssl
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
init(autoreset=True)

# ============================================================================
# CONFIGURATION
# ============================================================================

EMAIL_CREDENTIALS = [
    {'email': 'stillchaing9@gmail.com', 'app_password': 'xtvg mvnr qsdd ueeo'},
    {'email': 'badboistill@gmail.com', 'app_password': 'svwc rost swga pevv'},
    {'email': 'aynation700@gmail.com', 'app_password': 'ctte ysjm dssg adnp'},
    {'email': 'kingbadboi069@gmail.com', 'app_password': 'qgif nqls thrb zgbb'},
    {'email': 'badboistillchasing@gmail.com', 'app_password': 'clci bbst tgwj eijo'},
    {'email': 'managerhimself032@gmail.com', 'app_password': 'inagtgypnpyweleu'},
    {'email': 'arsheeqarsheeqq@gmail.com', 'app_password': 'pkkqfactxwkpvzgc'},
    {'email': 'unknownhimself6@gmail.com', 'app_password': 'uupfjdufriwrdgop'},
    {'email': 'cryptolord25ss@gmail.com', 'app_password': 'lczszqjxovvbuxco'},
    {'email': 'himselfdev759@gmail.com', 'app_password': 'fpwncioanqohseix'},
    {'email': 'chiefwanjoku9@gmail.com', 'app_password': 'qpub zfyx eswe mrhr'}
]

TELEGRAM_ABUSE_EMAILS = [
    "abuse@telegram.org", "spam@telegram.org", "dmca@telegram.org",
    "support@telegram.org", "recover@telegram.org", "childabuse@telegram.org",
    "terrorism@telegram.org", "legal@telegram.org", "security@telegram.org",
    "phishing@telegram.org", "abuse@telegram.org", "sticker@telegram.org"
]

# ============================================================================
# 50+ PROFESSIONAL REPORT MESSAGES - USER ACCOUNTS
# ============================================================================

USER_REPORT_MESSAGES = [
    # Spam and bots (1-10)
    """I am reporting the account @{username} for systematic spam and automated bot activity. This account has been posting identical promotional messages promoting cryptocurrency scams and adult content across 50+ public groups at regular intervals, indicating clear bot usage. The messages contain affiliate links and redirect to phishing websites. Group administrators in multiple communities have confirmed they are unable to stop this account's spam activity despite repeated bans. This violates Telegram's Terms of Service sections regarding spam, automated activity, and harmful content. I have documented over 200 instances of spam from this account with timestamps and screenshots. Requesting immediate review and permanent termination of this account to prevent further disruption to the Telegram community.""",
    
    """The account @{username} is engaged in large-scale spam operations targeting cryptocurrency communities. This account posts fake giveaways promising double payments, impersonating well-known figures in the crypto space. The account has been observed posting in over 100 different groups with the same copy-pasted messages. Multiple users have reported losing funds after interacting with the links shared by this account. The account uses automated posting tools to evade manual moderation and creates new accounts when banned. This is a coordinated spam operation causing financial harm to Telegram users. Please investigate and terminate this account immediately.""",
    
    """I am reporting @{username} for operating a network of spam bots. This account is part of a larger botnet that floods Telegram groups with unsolicited advertisements for illegal services including counterfeit documents, hacked accounts, and fraudulent investment schemes. The account posts the same content every 5-10 minutes across dozens of groups, making legitimate conversation impossible. The account's posting patterns are clearly automated and designed to bypass spam filters. This violates Telegram's policies against automation and spam. I request immediate account termination and investigation of the broader bot network.""",
    
    """The account @{username} is distributing malware through spam messages. This account posts links to malicious websites disguised as legitimate software downloads, cracked games, and adult content. When users click these links, they are prompted to download files that contain ransomware and information stealers. Multiple victims in my community have reported their computers infected and Telegram accounts compromised after interacting with this account's messages. The account changes its username frequently to avoid detection. This poses a serious security risk to all Telegram users. Please investigate and terminate this account urgently.""",
    
    """I am reporting @{username} for running a large-scale phishing operation. This account impersonates Telegram support and sends direct messages to users claiming their accounts will be deleted unless they verify through a fake login page. The phishing site captures usernames, passwords, and 2FA codes. I have identified over 50 users who have lost access to their accounts after interacting with this scam. The account uses Telegram's direct messaging system to target vulnerable users. This violates Telegram's policies against phishing and impersonation. Please terminate this account immediately and help affected users recover their accounts.""",
    
    # Harassment and threats (11-20)
    """I am writing to report the account @{username} for sustained harassment and stalking behavior. This individual has been sending threatening messages across multiple Telegram groups, including death threats and personal information leaks. They have posted my home address, workplace details, and photos of my family with explicit threats of violence. The user creates new accounts when blocked and continues the harassment across different communities. I have documented over 50 instances of this behavior with timestamps and screenshots, and have filed police reports in my jurisdiction. This violates Telegram's Terms of Service sections 8.2 (Violence) and 8.3 (Threats). I request immediate investigation and permanent suspension of this account to prevent further harm to multiple victims.""",
    
    """The account @{username} is coordinating a harassment campaign against journalists and activists. This account operates a private channel where members share personal information of targets, coordinate mass reporting attacks, and plan doxxing operations. Multiple individuals have been forced to delete their Telegram accounts and increase personal security due to credible threats originating from this account's network. The account administrators use Telegram's privacy features to evade detection and encourage members to create multiple accounts. This violates Telegram's policies against harassment, doxxing, and coordinated harmful behavior. I request immediate investigation and account termination.""",
    
    """I am reporting @{username} for making credible death threats against public figures. This account has posted detailed plans for assassination attempts, including timelines, locations, and methods. The account shared manifesto-style documents calling for violence and recruited others to participate. Multiple law enforcement agencies have been notified about these threats. This content poses immediate danger to public safety and violates Telegram's policies against violence and incitement. I have preserved screenshots and forwarded them to authorities. Please investigate urgently and terminate this account with data preservation for law enforcement.""",
    
    """The account @{username} is engaged in systematic cyberstalking. This account has been tracking my online activity for months, posting my real-time locations, commenting on my personal life, and sending threatening messages to my contacts. The account obtains private information through social engineering and shares it in public groups with calls for harassment. Despite blocking multiple accounts operated by this individual, they continue to create new profiles to continue the stalking. This is causing severe psychological distress and has forced me to limit my online presence. Telegram's reporting system is my only recourse. Please investigate and permanently ban this account and any associated accounts.""",
    
    """I am reporting @{username} for operating a revenge porn channel. This account distributes intimate images and videos of individuals without their consent, accompanied by personal information including full names, addresses, and workplace details. The victims have requested removal but the account refuses and continues to share the content. Multiple victims have been identified and some have reported job loss and relationship damage as a result. This is illegal in multiple jurisdictions and violates Telegram's policies on privacy and harassment. I have collected evidence including the original posts and victim statements. Please remove this content and ban the account permanently with data preservation for law enforcement.""",
    
    # Child safety (21-25)
    """I am urgently reporting @{username} for sharing Child Sexual Abuse Material (CSAM) in private Telegram groups. This account is using Telegram's infrastructure to distribute illegal content through encoded messages and external links. Multiple users have documented this activity and reported it to law enforcement. The account administrators use multiple layers of encryption and require verification to join their networks. This is a serious crime and Telegram's platform is being used to facilitate it. I request immediate account termination and preservation of all data for law enforcement investigation. This violates Telegram's zero-tolerance policy for child exploitation materials and may violate international laws.""",
    
    """The account @{username} has been observed grooming underage users in teen-oriented groups. This account messages minors, requests explicit photographs, and attempts to establish inappropriate relationships. Several community members have reported this account to moderators, and we have identified multiple underage victims. The account uses fake profiles and age misrepresentation to gain trust. This behavior constitutes grooming and puts minors at serious risk. Telegram must take immediate action to protect young users on its platform. Please investigate urgently and ban this account, preserving all chat history for law enforcement.""",
    
    # Financial scams (26-35)
    """I am reporting @{username} for operating a cryptocurrency investment scam. This account promises guaranteed returns of 200-300% within 24 hours and provides fake testimonials from "successful investors" using stolen profile photos. The account directs victims to send cryptocurrency to wallets it controls, then blocks users who ask questions or request withdrawals. I have identified over 100 victims who have lost amounts ranging from $100 to $50,000. The account operates multiple Telegram channels and groups to recruit new victims, with an estimated total fraud of over $2 million. This is a classic Ponzi scheme operating through Telegram. I request immediate investigation and account termination to prevent further victimization.""",
    
    """The account @{username} is running a fake investment bot scam. They advertise automated trading bots that supposedly generate passive income through cryptocurrency arbitrage. Victims are required to deposit a minimum of $250 to "activate" the bot, after which they receive fake screenshots of profits but are unable to withdraw funds. The account blocks users who attempt withdrawals and deletes negative comments. I have documented over 50 victims in a support group we created. The account changes its username frequently to avoid detection. This violates Telegram's policies against financial scams and fraudulent activities. Please investigate and terminate this account.""",
    
    """I am reporting @{username} for operating an illegal gambling operation through Telegram. The account hosts private channels where members place bets on sports, casino games, and political outcomes using cryptocurrency. The operation processes thousands of dollars daily and does not comply with any gambling regulations in any jurisdiction. Minors have been observed participating in these channels. The account administrators take a percentage of all bets and provide no consumer protections. This violates Telegram's policies against unlicensed gambling and financial crimes. I have documented the channel structure, payment methods, and participant screenshots. Please investigate and terminate this account.""",
    
    """The account @{username} is selling counterfeit goods including fake passports, driver's licenses, and identity documents. They advertise these services openly in public groups and use Telegram for customer communication and payment processing via cryptocurrency. The account claims to produce "undetectable" forgeries that pass all security checks. Multiple victims have reported paying hundreds of dollars and receiving nothing or poor-quality fakes that were immediately detected. This constitutes fraud and identity document trafficking, which are serious federal crimes in multiple countries. Please investigate and terminate this account immediately with data preservation for law enforcement.""",
    
    """The account @{username} is operating a loan scam targeting vulnerable individuals. They advertise "no credit check" loans with instant approval, then require an "processing fee" upfront. After victims pay the fee, the account blocks them and disappears. The account uses emotional manipulation, targeting people who post about financial difficulties in public groups. I have documented over 30 victims who have lost between $100 and $1000 each. The account changes its username and profile picture frequently to evade detection. This is predatory behavior causing real financial harm. Please investigate and terminate this account.""",
    
    # Copyright violations (36-40)
    """I am reporting @{username} for massive copyright infringement. This account distributes cracked commercial software including Adobe Creative Suite, Microsoft Windows, Autodesk products, and premium productivity tools worth over $100,000 in retail value. The account provides direct download links and crack instructions through Telegram channels with over 50,000 subscribers. Copyright holders including Adobe, Microsoft, and Autodesk have filed multiple complaints, but the account continues operating. This causes significant financial harm to software developers and violates Telegram's copyright policies. Please terminate this account and associated channels.""",
    
    """The account @{username} shares premium educational content from platforms including Udemy, MasterClass, and Coursera without authorization. They have posted over 500 courses worth over $50,000 in retail value, including content from exclusive instructors who rely on course sales for income. Multiple course creators have requested removal but the account continues posting new content daily. The account monetizes this piracy through advertising and premium membership fees. This constitutes significant copyright violation and intellectual property theft. Please review and take appropriate action to terminate this account.""",
    
    # Illegal goods (41-45)
    """I am reporting @{username} for operating a drug trafficking operation via Telegram. This account posts price lists for controlled substances including fentanyl, cocaine, methamphetamine, and prescription opioids, with cryptocurrency payment instructions and dead-drop delivery methods. The account has thousands of subscribers and facilitates dozens of transactions daily. Multiple overdose deaths have been linked to substances sold through this network according to law enforcement reports. This is a criminal enterprise operating through Telegram's infrastructure. I have documented transaction methods, user testimonials, and vendor communications. Please investigate and terminate this account immediately with data preservation for law enforcement.""",
    
    """The account @{username} shares detailed instructions for manufacturing illegal drugs and explosives. The content includes chemical recipes, precursor sources, step-by-step synthesis guides, and safety precautions for home laboratories. This material is accessible to minors and poses serious public safety risks. The account has been linked to multiple incidents where individuals attempted to manufacture these substances, resulting in injuries and property damage. This violates Telegram's policies against dangerous content and may violate international counter-terrorism laws. Please remove this content and ban the account permanently.""",
    
    """I am reporting @{username} for operating an illegal firearms marketplace. The account facilitates the sale of unregistered weapons, including automatic firearms, suppressors, and 3D-printed gun files. Sellers post photos and prices, then arrange meetings through encrypted chats. Multiple law enforcement agencies have documented firearms traced back to deals arranged through this account. The account uses coded language and cryptocurrency payments to evade detection. This is a serious crime and Telegram is being used as a platform for arms trafficking. Please investigate and terminate this account with data preservation for law enforcement.""",
    
    # Cybercrime (46-50)
    """The account @{username} is distributing ransomware-as-a-service. The account sells access to ransomware variants and provides technical support for deploying attacks. They offer step-by-step guides for encrypting victim files, demanding payment in cryptocurrency, and laundering the proceeds. Multiple hospitals, schools, and small businesses have been hit by ransomware traced back to this account's network. The account claims to have earned over $1 million in ransom payments. This is a serious cybercrime operation using Telegram as infrastructure. Please investigate and terminate this account immediately with data preservation for law enforcement.""",
    
    """I am reporting @{username} for operating a botnet command and control channel. The account distributes malware payloads and provides instructions for infected machines. Thousands of computers worldwide have been compromised through links shared by this account. The operator sells access to the botnet for DDoS attacks, credential harvesting, and cryptocurrency mining. The account uses Telegram's channels to communicate with botnet operators and distribute updates. This violates Telegram's policies against cyberattacks and malware distribution. Please investigate and terminate this account with data preservation.""",
    
    """The account @{username} is engaged in large-scale identity theft. They purchase stolen credential databases from data breaches and use Telegram to sell access to compromised accounts. Recent posts include data from major breaches affecting millions of users, complete with usernames, passwords, and credit card information. This information is being used for fraud, account takeover, and financial crimes. Victims have reported unauthorized transactions and identity fraud after their information was traded in this account's channels. This is a serious privacy violation and criminal activity. Please terminate this account immediately."""
]

# ============================================================================
# CHANNEL REPORT MESSAGES
# ============================================================================

CHANNEL_REPORT_MESSAGES = [
    """I am reporting the channel @{channel} for systematic copyright infringement on an industrial scale. This channel posts daily links to pirated movies, TV shows, and software, often within hours of official release. The channel has over 250,000 subscribers and generates significant revenue through advertisements and premium membership fees. Copyright holders including major studios and software companies have issued multiple takedown notices which have been ignored. The channel operators use mirror links and domain changes to evade blocks. This violates Telegram's copyright policy and causes significant financial harm to content creators. I request immediate channel termination and investigation of the operators.""",
    
    """The channel @{channel} is being used to coordinate illegal protest activities and incite violence against government institutions. Administrators post detailed plans for disrupting public services, targeting law enforcement, and damaging infrastructure. The channel has been linked to multiple violent incidents where followers carried out attacks discussed in the channel. This content poses immediate public safety risks and violates Telegram's policies against violence and illegal activities. Multiple law enforcement agencies have requested this content be removed. I request urgent investigation and channel removal with data preservation for authorities.""",
    
    """I am reporting the channel @{channel} for operating an unlicensed financial services scheme. The channel promotes high-yield investment programs, forex trading signals, and cryptocurrency "pump and dump" schemes. Subscribers pay monthly fees ranging from $50 to $500 for access to "exclusive" investment advice that has been documented as fraudulent. Multiple victims have reported significant financial losses, with some losing their life savings. The channel operators use fake testimonials and manipulated profit screenshots to attract new victims. This constitutes securities fraud and violates Telegram's policies against financial scams. Please investigate and terminate this channel.""",
    
    """This channel @{channel} is distributing child exploitation material through encoded messages and external links. Administrators use coded language and encrypted messaging to evade detection while coordinating inappropriate content. Multiple law enforcement agencies have been notified about this channel's activities and are actively investigating. The channel has been operating for over a year despite previous reports. This is a serious violation of Telegram's terms and potentially criminal activity. I request immediate investigation and channel termination with preservation of evidence for law enforcement.""",
    
    """The channel @{channel} is being used to coordinate distributed denial of service (DDoS) attacks against corporate and government websites. Administrators provide attack tools, target lists, and coordination instructions to thousands of subscribers. Several major websites have been taken offline as a result of attacks planned in this channel, causing millions in damages. The channel also shares stolen data from breached sites. This violates Telegram's policies against cyberattacks and may violate computer fraud laws in multiple countries. I request immediate channel removal and investigation of the administrators.""",
    
    """I am reporting @{channel} for systematic doxxing of private individuals. The channel publishes personal information including home addresses, phone numbers, workplace details, and family photos of journalists, activists, and private citizens who have criticized the channel's ideology. Victims have received credible threats and been forced to relocate or increase personal security. This ongoing harassment campaign has affected over 100 individuals documented in our records. The channel encourages followers to contact victims directly and has posted instructions for harassment. This violates Telegram's privacy policies and constitutes criminal harassment. Please terminate this channel immediately.""",
    
    """The channel @{channel} is distributing malware and ransomware through seemingly legitimate software downloads. Administrators pose as software developers offering cracked versions of popular applications, but the downloads contain trojans that encrypt user files and demand ransom. Multiple victims have reported losing access to critical business data and personal files. The channel has thousands of subscribers and has been operating for months. This is a large-scale cybercrime operation using Telegram as a distribution platform. Please investigate and terminate this channel with data preservation for law enforcement.""",
    
    """I am reporting the channel @{channel} for operating a large-scale counterfeit currency operation. Administrators sell counterfeit banknotes that pass basic security checks and provide shipping worldwide. The channel has thousands of subscribers and processes hundreds of orders monthly. They offer various denominations of multiple currencies and provide guarantees of successful passing. This constitutes counterfeiting, a serious federal crime in multiple jurisdictions. The operators use cryptocurrency payments and anonymous shipping to evade detection. Please investigate and terminate this channel with data preservation for law enforcement.""",
    
    """This channel @{channel} is being used to coordinate wildlife trafficking. Administrators facilitate the sale of endangered species, ivory, and exotic animal parts protected by CITES treaties. Sellers post photos and prices, then arrange shipping through encrypted messages. Multiple shipments traced to this channel have been intercepted by customs officials in different countries. This violates international conservation laws and Telegram's policies against illegal wildlife trade. Please investigate and terminate this channel with data preservation for authorities.""",
    
    """The channel @{channel} is distributing hacked databases containing personal information of millions of users. Recent posts include data breaches from major corporations, complete with usernames, passwords, email addresses, and credit card information. This information is being used for identity theft and fraud. The channel operators sell access to premium databases for cryptocurrency and have made hundreds of thousands in profits. This is a serious privacy violation and criminal activity. Please terminate this channel immediately with data preservation for law enforcement."""
]

# ============================================================================
# GROUP REPORT MESSAGES
# ============================================================================

GROUP_REPORT_MESSAGES = [
    """I am reporting the group @{group} for coordinating a large-scale drug trafficking operation. Administrators use the group to connect buyers with sellers, arrange meetups, and discuss pricing and quality of controlled substances including fentanyl, cocaine, methamphetamine, and prescription opioids. The group has over 5,000 members and facilitates dozens of transactions daily. Sellers provide reviews and ratings, and the group has established trust systems. This is a sophisticated criminal enterprise operating through Telegram's infrastructure. I have documented transaction methods, user testimonials, and vendor communications. Please investigate and terminate this group immediately with data preservation for law enforcement.""",
    
    """The group @{group} is being used to coordinate harassment and brigading campaigns against minority communities and vulnerable individuals. Members organize mass-reporting attacks, share personal information of targets, and coordinate downvote brigades on other platforms. The group administrators encourage members to create multiple accounts to evade blocks and provide templates for harassment messages. Multiple community leaders and private individuals have been forced offline due to this coordinated harassment, with some reporting psychological trauma. This violates Telegram's policies against hate speech, harassment, and coordinated harmful behavior. I request immediate investigation and group termination.""",
    
    """I am reporting the group @{group} for operating a large-scale counterfeit goods marketplace. Administrators facilitate the sale of fake designer goods, counterfeit electronics, forged documents, and replica luxury items. Sellers use the group to advertise products, negotiate prices, and arrange payment via cryptocurrency. The group has vendor ratings and dispute resolution systems. Multiple victims have reported receiving defective products or nothing at all after payment, with losses ranging from hundreds to thousands of dollars. This constitutes fraud and trademark infringement on a massive scale. Please investigate and terminate this group.""",
    
    """This group @{group} is being used to coordinate cyberattacks against critical infrastructure. Members share exploits targeting industrial control systems, power grids, water treatment facilities, and transportation networks. They discuss vulnerabilities in SCADA systems, share penetration testing methodologies, and coordinate attack timing. This poses a national security threat and violates Telegram's policies against cyberattacks. Multiple government agencies have been alerted to this group's activities. Please investigate and terminate this group immediately with data preservation.""",
    
    """The group @{group} is distributing child exploitation material through encrypted channels and coded language. Members share links to external sites hosting illegal content and discuss methods to evade law enforcement. The group administrators use multiple layers of encryption, require verification to join, and have strict rules about operational security. This is a serious crime and Telegram's platform is being used to facilitate it. Multiple law enforcement agencies are investigating this network. I request immediate investigation and group termination with data preservation for law enforcement.""",
    
    """I am reporting the group @{group} for operating a human trafficking recruitment network. Members post job offers that are actually covers for forced labor and sexual exploitation, and discuss methods for transporting victims across borders. The group provides instructions on creating false documentation and avoiding detection by authorities. Multiple victims have been identified who were recruited through this group, according to law enforcement reports. The operators use coded language and encrypted communications to evade detection. Please investigate and terminate this group immediately with data preservation.""",
    
    """The group @{group} is being used to coordinate insider trading and market manipulation. Members share non-public information about publicly traded companies, coordinate buying and selling to manipulate stock prices, and discuss methods for evading securities regulators. The group has been linked to multiple SEC investigations and has caused significant market disruptions. This violates securities laws in multiple countries and Telegram's policies against illegal financial activities. Please investigate and terminate this group with data preservation for regulatory authorities.""",
    
    """This group @{group} is distributing ransomware-as-a-service. Members purchase access to ransomware variants and receive technical support for deploying attacks. The group provides step-by-step guides for encrypting victim files, demanding payment in cryptocurrency, and laundering the proceeds through various services. Multiple hospitals, schools, and small businesses have been hit by ransomware traced back to this group. The operators claim to have made millions in ransom payments. This is a serious cybercrime operation. Please investigate and terminate this group immediately.""",
    
    """I am reporting the group @{group} for operating an illegal gambling ring. Members place bets on sports, casino games, political outcomes, and even reality TV shows using cryptocurrency. The group processes thousands of dollars daily and does not comply with any gambling regulations in any jurisdiction. Minors have been observed participating in the group's activities. The group administrators take a cut of all bets and provide no consumer protections or recourse for disputes. This violates Telegram's policies against unlicensed gambling. Please investigate and terminate this group.""",
    
    """The group @{group} is being used to coordinate election interference operations. Members discuss strategies for spreading disinformation, hacking voter databases, intimidating election officials, and coordinating voting manipulation. The group has been linked to multiple foreign intelligence agencies and has been cited in intelligence reports. This poses a threat to democratic processes and violates Telegram's policies against political interference and coordinated inauthentic behavior. Please investigate and terminate this group with data preservation for authorities."""
]

# ============================================================================
# PROXY MANAGER - MAIN PROXY FILE (Proxies.txt)
# ============================================================================

class ProxyManager:
    """Manages ALL proxies (stored in Proxies.txt) - for email and general use"""
    
    def __init__(self, filename="Proxies.txt"):
        self.filename = filename
        self.proxies = []
        self.working_proxies = []
        self.failed_proxies = set()
        self.current_index = 0
        self.lock = threading.Lock()
        self.load_proxies()
    
    def load_proxies(self):
        """Load proxies from main Proxies.txt file"""
        try:
            if os.path.exists(self.filename):
                with open(self.filename, 'r') as f:
                    self.proxies = [line.strip() for line in f if line.strip() and not line.startswith('#')]
                print(f"{Fore.GREEN}[📁] Loaded {len(self.proxies)} proxies from {self.filename}")
                self.working_proxies = self.proxies.copy()
            else:
                print(f"{Fore.YELLOW}[⚠️] {self.filename} not found - creating empty file")
                open(self.filename, 'w').close()
                self.proxies = []
                self.working_proxies = []
        except Exception as e:
            print(f"{Fore.RED}[❌] Error loading proxies: {e}")
            self.proxies = []
            self.working_proxies = []
    
    def save_proxies(self):
        """Save working proxies back to main file"""
        try:
            with open(self.filename, 'w') as f:
                for proxy in self.working_proxies:
                    f.write(f"{proxy}\n")
            print(f"{Fore.GREEN}[💾] Saved {len(self.working_proxies)} working proxies to {self.filename}")
        except Exception as e:
            print(f"{Fore.RED}[❌] Error saving proxies: {e}")
    
    def get_next_proxy(self):
        """Get next working proxy in rotation"""
        with self.lock:
            if not self.working_proxies:
                return None
            if self.current_index >= len(self.working_proxies):
                self.current_index = 0
            proxy = self.working_proxies[self.current_index]
            self.current_index += 1
            return proxy
    
    def mark_failed(self, proxy):
        """Mark a proxy as failed and remove from rotation"""
        with self.lock:
            if proxy in self.working_proxies:
                self.working_proxies.remove(proxy)
                self.failed_proxies.add(proxy)
                print(f"{Fore.RED}[❌] Proxy failed - removed: {proxy}")
    
    def mark_success(self, proxy):
        """Proxy worked - keep in rotation"""
        pass
    
    def add_proxies(self, new_proxies):
        """Add new proxies to the list"""
        with self.lock:
            for proxy in new_proxies:
                if proxy not in self.proxies and proxy not in self.working_proxies:
                    self.proxies.append(proxy)
                    self.working_proxies.append(proxy)
            self.save_proxies()
    
    def get_stats(self):
        """Get proxy statistics"""
        return {
            'total': len(self.proxies),
            'working': len(self.working_proxies),
            'failed': len(self.failed_proxies)
        }
    
    def parse_proxy(self, proxy_str):
        """Parse proxy string for SOCKS"""
        try:
            if '@' in proxy_str:
                auth, hostport = proxy_str.split('@')
                if ':' in auth:
                    username, password = auth.split(':', 1)
                else:
                    username, password = auth, ''
                host, port = hostport.split(':')
            else:
                host, port = proxy_str.split(':')
                username, password = None, None
            port = int(port)
            return host, port, username, password
        except Exception as e:
            return None, None, None, None

# ============================================================================
# HTTPS PROXY MANAGER - FOR WEB REPORTS ONLY (https.txt)
# ============================================================================

class HttpsProxyManager:
    """Manages HTTPS proxies ONLY (stored in https.txt) - for web reports"""
    
    def __init__(self, filename="https.txt"):
        self.filename = filename
        self.proxies = []
        self.working_proxies = []
        self.failed_proxies = set()
        self.current_index = 0
        self.lock = threading.Lock()
        self.load_proxies()
    
    def load_proxies(self):
        """Load HTTPS proxies from https.txt"""
        try:
            if os.path.exists(self.filename):
                with open(self.filename, 'r') as f:
                    self.proxies = [line.strip() for line in f if line.strip() and not line.startswith('#')]
                print(f"{Fore.GREEN}[🔒] Loaded {len(self.proxies)} HTTPS proxies from {self.filename}")
                self.working_proxies = self.proxies.copy()
            else:
                print(f"{Fore.YELLOW}[⚠️] {self.filename} not found - creating empty file")
                open(self.filename, 'w').close()
                self.proxies = []
                self.working_proxies = []
        except Exception as e:
            print(f"{Fore.RED}[❌] Error loading HTTPS proxies: {e}")
            self.proxies = []
            self.working_proxies = []
    
    def save_proxies(self):
        """Save working HTTPS proxies back to file"""
        try:
            with open(self.filename, 'w') as f:
                for proxy in self.working_proxies:
                    f.write(f"{proxy}\n")
            print(f"{Fore.GREEN}[💾] Saved {len(self.working_proxies)} working HTTPS proxies to {self.filename}")
        except Exception as e:
            print(f"{Fore.RED}[❌] Error saving HTTPS proxies: {e}")
    
    def get_next_proxy(self):
        """Get next working HTTPS proxy"""
        with self.lock:
            if not self.working_proxies:
                return None
            if self.current_index >= len(self.working_proxies):
                self.current_index = 0
            proxy = self.working_proxies[self.current_index]
            self.current_index += 1
            return proxy
    
    def mark_failed(self, proxy):
        """Mark HTTPS proxy as failed"""
        with self.lock:
            if proxy in self.working_proxies:
                self.working_proxies.remove(proxy)
                self.failed_proxies.add(proxy)
                print(f"{Fore.RED}[❌] HTTPS proxy failed - removed: {proxy}")
    
    def get_proxy_dict(self, proxy_str):
        """Convert HTTPS proxy string to requests format"""
        if not proxy_str:
            return None
        try:
            if '@' in proxy_str:
                auth, server = proxy_str.split('@')
                return {
                    'http': f'http://{auth}@{server}',
                    'https': f'http://{auth}@{server}'
                }
            else:
                return {
                    'http': f'http://{proxy_str}',
                    'https': f'http://{proxy_str}'
                }
        except:
            return None
    
    def get_stats(self):
        """Get HTTPS proxy statistics"""
        return {
            'total': len(self.proxies),
            'working': len(self.working_proxies),
            'failed': len(self.failed_proxies)
        }

# ============================================================================
# PROXY HARVESTER
# ============================================================================

class ProxyHarvester:
    """Harvest proxies from multiple sources"""
    
    def __init__(self):
        self.sources = [
            "https://api.proxyscrape.com/v2/?request=getproxies&protocol=http&timeout=10000&country=all",
            "https://api.proxyscrape.com/v2/?request=getproxies&protocol=socks4&timeout=10000&country=all",
            "https://api.proxyscrape.com/v2/?request=getproxies&protocol=socks5&timeout=10000&country=all",
            "https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt",
            "https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks4.txt",
            "https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks5.txt",
            "https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/http.txt",
            "https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/socks4.txt",
            "https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/socks5.txt",
        ]
        
        self.https_sources = [
            "https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt",
            "https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/http.txt",
            "https://api.proxyscrape.com/v2/?request=getproxies&protocol=http&timeout=10000&country=all",
            "https://raw.githubusercontent.com/ShiftyTR/Proxy-List/master/http.txt",
            "https://www.proxy-list.download/api/v1/get?type=http",
            "https://www.proxy-list.download/api/v1/get?type=https",
        ]
        
        self.session = requests.Session()
        self.session.verify = False
    
    def extract_proxies(self, text):
        """Extract IP:port pairs"""
        proxies = []
        pattern = r'\b(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?):\d{2,5}\b'
        matches = re.findall(pattern, text)
        
        for proxy in matches:
            try:
                ip, port = proxy.split(':')
                port = int(port)
                if 1 <= port <= 65535:
                    proxies.append(proxy)
            except:
                continue
        
        return list(set(proxies))
    
    def test_proxy(self, proxy, proxy_type="general"):
        """Test if a proxy works"""
        proxies = {
            'http': f'http://{proxy}',
            'https': f'http://{proxy}'
        }
        
        try:
            response = requests.get(
                'http://httpbin.org/ip',
                proxies=proxies,
                timeout=8,
                verify=False
            )
            if response.status_code == 200:
                return True
        except:
            pass
        
        return False
    
    def harvest_general(self, quick=True):
        """Harvest proxies for general use (Proxies.txt)"""
        print(f"\n{Fore.CYAN}[🌐] Harvesting general proxies...")
        all_proxies = []
        sources = self.sources[:3] if quick else self.sources
        
        for url in sources:
            try:
                print(f"{Fore.YELLOW}[↻] Fetching: {url.split('/')[-1]}...", end='')
                response = self.session.get(url, timeout=15)
                if response.status_code == 200:
                    proxies = self.extract_proxies(response.text)
                    all_proxies.extend(proxies)
                    print(f"\r{Fore.GREEN}[✅] {url.split('/')[-1]:<30} → {len(proxies):>4} proxies")
                else:
                    print(f"\r{Fore.RED}[❌] {url.split('/')[-1]:<30} → Failed")
            except:
                print(f"\r{Fore.RED}[❌] {url.split('/')[-1]:<30} → Error")
        
        return list(set(all_proxies))
    
    def harvest_https(self, quick=True):
        """Harvest HTTPS-only proxies (https.txt)"""
        print(f"\n{Fore.CYAN}[🔒] Harvesting HTTPS proxies...")
        all_proxies = []
        sources = self.https_sources[:3] if quick else self.https_sources
        
        for url in sources:
            try:
                print(f"{Fore.YELLOW}[↻] Fetching: {url.split('/')[-1]}...", end='')
                response = self.session.get(url, timeout=15)
                if response.status_code == 200:
                    proxies = self.extract_proxies(response.text)
                    all_proxies.extend(proxies)
                    print(f"\r{Fore.GREEN}[✅] {url.split('/')[-1]:<30} → {len(proxies):>4} HTTPS proxies")
                else:
                    print(f"\r{Fore.RED}[❌] {url.split('/')[-1]:<30} → Failed")
            except:
                print(f"\r{Fore.RED}[❌] {url.split('/')[-1]:<30} → Error")
        
        return list(set(all_proxies))
    
    def test_batch(self, proxies, max_workers=50):
        """Test multiple proxies"""
        print(f"\n{Fore.CYAN}[⚡] Testing {len(proxies)} proxies...")
        
        working = []
        total = len(proxies)
        
        with concurrent.futures.ThreadPoolExecutor(max_workers=max_workers) as executor:
            future_to_proxy = {executor.submit(self.test_proxy, proxy): proxy for proxy in proxies}
            
            for i, future in enumerate(concurrent.futures.as_completed(future_to_proxy), 1):
                proxy = future_to_proxy[future]
                try:
                    if future.result():
                        working.append(proxy)
                        print(f"{Fore.GREEN}[✅] Working: {proxy}")
                    else:
                        print(f"{Fore.RED}[❌] Failed: {proxy}")
                except:
                    print(f"{Fore.RED}[❌] Error: {proxy}")
                
                percent = (i / total) * 100
                bar = '█' * int(percent / 2) + '░' * (50 - int(percent / 2))
                print(f"\r{Fore.YELLOW}[{bar}] {percent:.1f}% ({i}/{total})", end='')
        
        print(f"\n{Fore.GREEN}[📊] Working proxies: {len(working)}/{total}")
        return working

# ============================================================================
# REAL EMAIL BOMBER (Uses Proxies.txt)
# ============================================================================

class RealEmailBomber:
    """Email bomber using Proxies.txt for SOCKS rotation"""
    
    def __init__(self, proxy_manager):
        self.proxy_manager = proxy_manager
        self.stats = {'sent': 0, 'failed': 0, 'by_account': {}}
    
    def send_via_proxy(self, email_config, to_emails, subject, body, proxy_str):
        """Send email through SOCKS proxy"""
        host, port, username, password = self.proxy_manager.parse_proxy(proxy_str)
        if not host:
            return False, "Invalid proxy"
        
        original_socket = socket.socket
        original_create_connection = socket.create_connection
        
        try:
            socks.set_default_proxy(socks.SOCKS5, host, port, username=username, password=password)
            socket.socket = socks.socksocket
            socket.create_connection = socks.create_connection
            
            msg = MIMEMultipart('alternative')
            msg['From'] = email_config['email']
            msg['To'] = ', '.join(to_emails[:3])
            msg['Subject'] = subject
            msg['Date'] = datetime.now().strftime('%a, %d %b %Y %H:%M:%S %z')
            msg.attach(MIMEText(body, 'plain', 'utf-8'))
            
            server = smtplib.SMTP('smtp.gmail.com', 587, timeout=30)
            server.starttls()
            server.login(email_config['email'], email_config['app_password'])
            server.send_message(msg)
            server.quit()
            
            socket.socket = original_socket
            socket.create_connection = original_create_connection
            socks.set_default_proxy()
            
            return True, "Success"
            
        except Exception as e:
            socket.socket = original_socket
            socket.create_connection = original_create_connection
            socks.set_default_proxy()
            return False, str(e)
    
    def send_direct(self, email_config, to_emails, subject, body):
        """Send directly (fallback)"""
        try:
            msg = MIMEMultipart('alternative')
            msg['From'] = email_config['email']
            msg['To'] = ', '.join(to_emails[:3])
            msg['Subject'] = subject
            msg.attach(MIMEText(body, 'plain', 'utf-8'))
            
            server = smtplib.SMTP('smtp.gmail.com', 587, timeout=30)
            server.starttls()
            server.login(email_config['email'], email_config['app_password'])
            server.send_message(msg)
            server.quit()
            
            return True, "Success"
        except Exception as e:
            return False, str(e)
    
    def attack(self, target, report_type, report_message, max_reports=None):
        """Launch email attack using Proxies.txt rotation"""
        print(f"\n{Fore.RED}{'═'*70}")
        print(f"{Fore.YELLOW}[📧] EMAIL ATTACK - Using Proxies.txt")
        print(f"{Fore.RED}{'═'*70}")
        
        stats = self.proxy_manager.get_stats()
        print(f"{Fore.CYAN}[🔌] Available proxies: {stats['working']}")
        
        sent = 0
        failed = 0
        email_index = 0
        
        while True:
            if max_reports and sent >= max_reports:
                break
            
            email_config = EMAIL_CREDENTIALS[email_index % len(EMAIL_CREDENTIALS)]
            email_index += 1
            
            proxy = self.proxy_manager.get_next_proxy()
            proxy_info = f"via {proxy}" if proxy else "direct"
            
            subject = f"URGENT: {report_type} @{target} - Case #{random.randint(10000,99999)}"
            body = report_message.format(username=target)
            
            print(f"\n{Fore.CYAN}[📤] Sending from {email_config['email']} {proxy_info}")
            
            if proxy:
                success, msg = self.send_via_proxy(email_config, TELEGRAM_ABUSE_EMAILS, subject, body, proxy)
            else:
                success, msg = self.send_direct(email_config, TELEGRAM_ABUSE_EMAILS, subject, body)
            
            if success:
                sent += 1
                print(f"{Fore.GREEN}[✅] Report #{sent} sent successfully")
                if proxy:
                    self.proxy_manager.mark_success(proxy)
            else:
                failed += 1
                print(f"{Fore.RED}[❌] Failed: {msg[:50]}")
                if proxy:
                    self.proxy_manager.mark_failed(proxy)
            
            delay = random.uniform(3, 7)
            print(f"{Fore.YELLOW}[⏱️] Waiting {delay:.1f}s...")
            time.sleep(delay)
            
            if sent % 10 == 0:
                self.proxy_manager.save_proxies()
        
        self.stats = {'sent': sent, 'failed': failed}
        return sent, failed

# ============================================================================
# WEB REPORTER - USES HTTPS.TXT ONLY
# ============================================================================

class WebReporter:
    """Web reporter using https.txt for HTTPS proxies ONLY"""
    
    def __init__(self, https_manager):
        self.https_manager = https_manager
        self.session = requests.Session()
        
        retry = Retry(total=2, backoff_factor=0.5)
        adapter = HTTPAdapter(max_retries=retry)
        self.session.mount('http://', adapter)
        self.session.mount('https://', adapter)
        
        self.report_urls = [
            "https://telegram.org/support",
            "https://telegram.org/abuse",
            "https://telegram.org/support/report",
            "https://telegram.org/abuse/report",
            "https://telegram.org/report",
            "https://telegram.org/moderation"
        ]
        
        self.user_agents = [
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/120.0.0.0",
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 Safari/605.1.15",
            "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 Chrome/119.0.0.0",
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:121.0) Gecko/20100101 Firefox/121.0",
        ]
    
    def send_report(self, target, report_type, report_message):
        """Send web report using HTTPS proxy from https.txt"""
        
        proxy_str = self.https_manager.get_next_proxy()
        proxy_dict = self.https_manager.get_proxy_dict(proxy_str)
        proxy_info = f"via {proxy_str}" if proxy_str else "direct"
        
        headers = {
            'User-Agent': random.choice(self.user_agents),
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Accept-Language': 'en-US,en;q=0.9',
            'Content-Type': 'application/x-www-form-urlencoded',
        }
        
        data = {
            'message': report_message[:3000],
            'submit': 'Submit Report',
            'peer': f'@{target}',
            'reason': 'spam'
        }
        
        urls = random.sample(self.report_urls, len(self.report_urls))
        
        for url in urls:
            try:
                response = self.session.post(
                    url,
                    data=data,
                    headers=headers,
                    proxies=proxy_dict,
                    timeout=15,
                    verify=False
                )
                
                if response.status_code in [200, 201, 202, 204, 302]:
                    if proxy_str:
                        self.https_manager.mark_success(proxy_str)
                    return True, f"Success via {url.split('/')[-1]} {proxy_info}"
                    
            except Exception as e:
                continue
        
        if proxy_str:
            self.https_manager.mark_failed(proxy_str)
        return False, f"Failed {proxy_info}"
    
    def attack(self, target, report_type, report_message, count=50):
        """Launch web attack using ONLY https.txt proxies"""
        
        print(f"\n{Fore.BLUE}{'═'*70}")
        print(f"{Fore.YELLOW}[🌐] WEB ATTACK - Using https.txt ONLY")
        print(f"{Fore.BLUE}{'═'*70}")
        
        stats = self.https_manager.get_stats()
        print(f"{Fore.CYAN}[🔒] HTTPS proxies available: {stats['working']}")
        print(f"{Fore.CYAN}[🔢] Reports to send: {count}")
        
        successful = 0
        failed = 0
        
        for i in range(1, count + 1):
            print(f"\r{Fore.CYAN}[📤] Sending web report {i}/{count}...", end='')
            
            if report_type == 'user':
                formatted = report_message.format(username=target)
            elif report_type == 'channel':
                formatted = report_message.format(channel=target)
            else:
                formatted = report_message.format(group=target)
            
            success, msg = self.send_report(target, report_type, formatted)
            
            if success:
                successful += 1
                print(f"\r{Fore.GREEN}[✅] Web report {i}/{count} successful        ")
            else:
                failed += 1
                print(f"\r{Fore.RED}[❌] Web report {i}/{count} failed            ")
            
            delay = random.uniform(4, 9)
            time.sleep(delay)
            
            if i % 10 == 0:
                self.https_manager.save_proxies()
        
        print(f"\n{Fore.GREEN}[📊] Web reports: {successful} successful, {failed} failed")
        return successful, failed

# ============================================================================
# MAIN ZISKY TOOL
# ============================================================================

class ZiskyTGBanTool:
    """Main Zisky Telegram Ban Tool"""
    
    def __init__(self):
        self.proxy_manager = ProxyManager("Proxies.txt")        # For email
        self.https_manager = HttpsProxyManager("https.txt")     # For web ONLY
        self.harvester = ProxyHarvester()
        self.email_bomber = RealEmailBomber(self.proxy_manager)
        self.web_reporter = WebReporter(self.https_manager)
        self.start_time = datetime.now()
    
    def print_banner(self):
        """Print Zisky banner"""
        os.system('clear' if os.name != 'nt' else 'cls')
        
        print(f"{Fore.RED}╔══════════════════════════════════════════════════════════════════════════════╗")
        print(f"{Fore.RED}║                                                                              ║")
        print(f"{Fore.RED}║   ███████╗██╗███████╗██╗  ██╗██╗   ██╗    ████████╗ ██████╗     ██████╗ █████╗ ██╗   ██╗")
        print(f"{Fore.YELLOW}║   ╚══███╔╝██║██╔════╝██║ ██╔╝██║   ██║    ╚══██╔══╝██╔═══██╗    ██╔══██╗██╔══██╗██║   ██║")
        print(f"{Fore.GREEN}║     ███╔╝ ██║███████╗█████╔╝ ██║   ██║       ██║   ██║   ██║    ██████╔╝███████║██║   ██║")
        print(f"{Fore.CYAN}║    ███╔╝  ██║╚════██║██╔═██╗ ██║   ██║       ██║   ██║   ██║    ██╔══██╗██╔══██║╚██╗ ██╔╝")
        print(f"{Fore.MAGENTA}║   ███████╗██║███████║██║  ██╗╚██████╔╝       ██║   ╚██████╔╝    ██║  ██║██║  ██║ ╚████╔╝ ")
        print(f"{Fore.RED}║   ╚══════╝╚═╝╚══════╝╚═╝  ╚═╝ ╚═════╝        ╚═╝    ╚═════╝     ╚═╝  ╚═╝╚═╝  ╚═╝  ╚═══╝  ")
        print(f"{Fore.RED}║                                                                              ║")
        print(f"{Fore.YELLOW}║                    🔥 TELEGRAM MASS REPORTING TOOL v4.0 🔥                    ║")
        print(f"{Fore.GREEN}║              📧 EMAIL: Proxies.txt • 🌐 WEB: https.txt • 🔄 DUAL FILES          ║")
        print(f"{Fore.CYAN}║                    ⚡ 50+ PROFESSIONAL REPORT MESSAGES ⚡                         ║")
        print(f"{Fore.RED}║                                                                              ║")
        print(f"{Fore.RED}╚══════════════════════════════════════════════════════════════════════════════╝")
        print()
        
        proxy_stats = self.proxy_manager.get_stats()
        https_stats = self.https_manager.get_stats()
        
        print(f"{Fore.CYAN}[⚙️] System Status:")
        print(f"{Fore.CYAN}    📁 Proxies.txt (Email): {proxy_stats['working']}/{proxy_stats['total']} working")
        print(f"{Fore.CYAN}    🔒 https.txt (Web): {https_stats['working']}/{https_stats['total']} working")
        print(f"{Fore.CYAN}    📧 Email accounts: {len(EMAIL_CREDENTIALS)}")
        print(f"{Fore.CYAN}    📝 Report templates: {len(USER_REPORT_MESSAGES)} Users, {len(CHANNEL_REPORT_MESSAGES)} Channels, {len(GROUP_REPORT_MESSAGES)} Groups")
        print()
    
    def proxy_menu(self):
        """Proxy management menu"""
        while True:
            print(f"\n{Fore.CYAN}{'═'*70}")
            print(f"{Fore.YELLOW}[🔌] PROXY MANAGEMENT")
            print(f"{Fore.CYAN}{'═'*70}")
            
            proxy_stats = self.proxy_manager.get_stats()
            https_stats = self.https_manager.get_stats()
            
            print(f"\n{Fore.GREEN}Current Status:")
            print(f"  {Fore.CYAN}📁 Proxies.txt (Email): {proxy_stats['working']}/{proxy_stats['total']}")
            print(f"  {Fore.CYAN}🔒 https.txt (Web): {https_stats['working']}/{https_stats['total']}")
            
            print(f"\n{Fore.YELLOW}Options:")
            print(f"  {Fore.GREEN}[1] Harvest proxies for Proxies.txt (Email + General)")
            print(f"  {Fore.GREEN}[2] Harvest HTTPS proxies for https.txt (Web Only)")
            print(f"  {Fore.GREEN}[3] Test all proxies in Proxies.txt")
            print(f"  {Fore.GREEN}[4] Test all proxies in https.txt")
            print(f"  {Fore.GREEN}[5] View proxy lists")
            print(f"  {Fore.GREEN}[6] Return to main menu")
            
            choice = input(f"\n{Fore.YELLOW}[?] Select: ").strip()
            
            if choice == '1':
                proxies = self.harvester.harvest_general(quick=True)
                if proxies:
                    working = self.harvester.test_batch(proxies)
                    self.proxy_manager.add_proxies(working)
            
            elif choice == '2':
                proxies = self.harvester.harvest_https(quick=True)
                if proxies:
                    working = self.harvester.test_batch(proxies)
                    for proxy in working:
                        if proxy not in self.https_manager.proxies:
                            self.https_manager.proxies.append(proxy)
                            self.https_manager.working_proxies.append(proxy)
                    self.https_manager.save_proxies()
            
            elif choice == '3':
                if self.proxy_manager.proxies:
                    working = self.harvester.test_batch(self.proxy_manager.proxies)
                    self.proxy_manager.working_proxies = working
                    self.proxy_manager.save_proxies()
            
            elif choice == '4':
                if self.https_manager.proxies:
                    working = self.harvester.test_batch(self.https_manager.proxies)
                    self.https_manager.working_proxies = working
                    self.https_manager.save_proxies()
            
            elif choice == '5':
                print(f"\n{Fore.CYAN}Proxies.txt (Email):")
                for i, p in enumerate(self.proxy_manager.working_proxies[:10], 1):
                    print(f"  {Fore.GREEN}{i}. {p}")
                print(f"\n{Fore.CYAN}https.txt (Web):")
                for i, p in enumerate(self.https_manager.working_proxies[:10], 1):
                    print(f"  {Fore.GREEN}{i}. {p}")
                input(f"\n{Fore.YELLOW}[Press Enter...]")
            
            elif choice == '6':
                break
    
    def attack_menu(self):
        """Attack menu"""
        print(f"\n{Fore.CYAN}{'═'*70}")
        print(f"{Fore.YELLOW}[⚔️] ATTACK MENU")
        print(f"{Fore.CYAN}{'═'*70}")
        
        print(f"\n{Fore.GREEN}Target types:")
        print(f"  {Fore.CYAN}[1] User Account (@username)")
        print(f"  {Fore.CYAN}[2] Channel (@channel)")
        print(f"  {Fore.CYAN}[3] Group (@group)")
        
        type_choice = input(f"\n{Fore.YELLOW}[?] Select target type (1-3): ").strip()
        type_map = {'1': 'user', '2': 'channel', '3': 'group'}
        report_type = type_map.get(type_choice, 'user')
        
        target = input(f"{Fore.YELLOW}[?] Enter target @username (without @): ").strip()
        
        # Message selection
        print(f"\n{Fore.GREEN}Message options:")
        print(f"  {Fore.CYAN}[1] Use random message")
        print(f"  {Fore.CYAN}[2] Browse messages")
        print(f"  {Fore.CYAN}[3] Custom message")
        
        msg_choice = input(f"\n{Fore.YELLOW}[?] Select (1-3): ").strip()
        
        if msg_choice == '2':
            if report_type == 'user':
                messages = USER_REPORT_MESSAGES
                print(f"\n{Fore.CYAN}User Messages (1-{len(messages)}):")
                for i, msg in enumerate(messages[:10], 1):
                    preview = msg[:100].replace('{username}', target) + "..."
                    print(f"  {Fore.GREEN}[{i}] {preview}")
                if len(messages) > 10:
                    print(f"  {Fore.YELLOW}... and {len(messages)-10} more")
                msg_idx = int(input(f"\n{Fore.YELLOW}[?] Select message number (1-{len(messages)}): ")) - 1
                report_message = messages[msg_idx]
            elif report_type == 'channel':
                messages = CHANNEL_REPORT_MESSAGES
                msg_idx = random.randint(0, len(messages)-1)
                report_message = messages[msg_idx]
            else:
                messages = GROUP_REPORT_MESSAGES
                msg_idx = random.randint(0, len(messages)-1)
                report_message = messages[msg_idx]
        elif msg_choice == '3':
            report_message = input(f"{Fore.YELLOW}[?] Enter custom message: ").strip()
        else:
            if report_type == 'user':
                report_message = random.choice(USER_REPORT_MESSAGES)
            elif report_type == 'channel':
                report_message = random.choice(CHANNEL_REPORT_MESSAGES)
            else:
                report_message = random.choice(GROUP_REPORT_MESSAGES)
        
        print(f"\n{Fore.GREEN}Attack types:")
        print(f"  {Fore.CYAN}[1] Email bombing (Proxies.txt)")
        print(f"  {Fore.CYAN}[2] Web reporting (https.txt)")
        print(f"  {Fore.CYAN}[3] Combined attack")
        
        attack_choice = input(f"\n{Fore.YELLOW}[?] Select attack type (1-3): ").strip()
        
        count = input(f"{Fore.YELLOW}[?] Reports to send (Enter for unlimited): ").strip()
        count = int(count) if count.isdigit() else None
        
        # Confirmation
        print(f"\n{Fore.RED}{'═'*70}")
        print(f"{Fore.YELLOW}[⚠️] ATTACK CONFIRMATION")
        print(f"{Fore.RED}{'═'*70}")
        print(f"{Fore.CYAN}Target: @{target} ({report_type})")
        print(f"{Fore.CYAN}Attack: {['Email','Web','Combined'][int(attack_choice)-1]}")
        print(f"{Fore.CYAN}Reports: {count if count else 'Unlimited'}")
        
        confirm = input(f"\n{Fore.YELLOW}[?] Launch attack? (y/N): ").strip().lower()
        
        if confirm != 'y':
            print(f"{Fore.YELLOW}[⚠️] Attack cancelled")
            return
        
        print(f"\n{Fore.RED}[🚀] ATTACK LAUNCHED AT {datetime.now().strftime('%H:%M:%S')}")
        
        if attack_choice == '1':
            self.email_bomber.attack(target, report_type, report_message, count)
        elif attack_choice == '2':
            self.web_reporter.attack(target, report_type, report_message, count or 50)
        else:
            email_thread = threading.Thread(
                target=self.email_bomber.attack,
                args=(target, report_type, report_message, count)
            )
            email_thread.start()
            self.web_reporter.attack(target, report_type, report_message, count or 30)
            email_thread.join()
    
    def run(self):
        """Main loop"""
        self.print_banner()
        
        while True:
            print(f"\n{Fore.CYAN}{'═'*70}")
            print(f"{Fore.YELLOW}[🏠] MAIN MENU")
            print(f"{Fore.CYAN}{'═'*70}")
            
            print(f"\n{Fore.GREEN}[1] Launch Attack")
            print(f"{Fore.GREEN}[2] Proxy Management")
            print(f"{Fore.GREEN}[3] View Statistics")
            print(f"{Fore.GREEN}[4] GitHub Setup Guide")
            print(f"{Fore.GREEN}[5] Exit")
            
            choice = input(f"\n{Fore.YELLOW}[?] Select: ").strip()
            
            if choice == '1':
                self.attack_menu()
            elif choice == '2':
                self.proxy_menu()
            elif choice == '3':
                proxy_stats = self.proxy_manager.get_stats()
                https_stats = self.https_manager.get_stats()
                print(f"\n{Fore.CYAN}Proxies.txt: {proxy_stats['working']}/{proxy_stats['total']}")
                print(f"{Fore.CYAN}https.txt: {https_stats['working']}/{https_stats['total']}")
                input(f"\n{Fore.YELLOW}[Press Enter...]")
            elif choice == '4':
                show_github_setup()
            elif choice == '5':
                print(f"\n{Fore.GREEN}[👋] Thanks for using Zisky TG Ban Tool!")
                print(f"{Fore.YELLOW}[🔒] Stay anonymous, stay secure.")
                break

# ============================================================================
# GITHUB SETUP INSTRUCTIONS
# ============================================================================

def show_github_setup():
    """Display GitHub setup instructions"""
    print(f"\n{Fore.CYAN}{'═'*70}")
    print(f"{Fore.YELLOW}[🐙] GITHUB SETUP INSTRUCTIONS")
    print(f"{Fore.CYAN}{'═'*70}")
    
    print(f"""
{Fore.GREEN}╔════════════════════════════════════════════════════════════════╗
║                    GITHUB REPOSITORY SETUP                        ║
╚════════════════════════════════════════════════════════════════════╝

{Fore.YELLOW}STEP 1: Create GitHub Repository{Style.RESET_ALL}
{Fore.CYAN}────────────────────────────────────────────────────────────────
1. Go to https://github.com/new
2. Repository name: {Fore.GREEN}zisky-tg-ban{Fore.CYAN}
3. Description: Telegram Mass Reporting Tool with Proxy Support
4. Choose: {Fore.GREEN}Public{Fore.CYAN}
5. Click "Create repository"

{Fore.YELLOW}STEP 2: Upload Files{Style.RESET_ALL}
{Fore.CYAN}────────────────────────────────────────────────────────────────
1. In your new repository, click "Add file" → "Upload files"
2. Upload this script as: {Fore.GREEN}main.py{Fore.CYAN}
3. Create these empty files:
   • {Fore.GREEN}Proxies.txt{Fore.CYAN} - Add your SOCKS5/HTTP proxies
   • {Fore.GREEN}https.txt{Fore.CYAN} - Add your HTTPS proxies
   • {Fore.GREEN}README.md{Fore.CYAN} - Add documentation
4. Commit changes

{Fore.YELLOW}STEP 3: Clone in Termux{Style.RESET_ALL}
{Fore.CYAN}────────────────────────────────────────────────────────────────
cd ~
git clone https://github.com/hizisaac6-coder/zisky-tg-ban.git
cd zisky-tg-ban
pip install requests colorama pysocks urllib3
python main.py

{Fore.YELLOW}STEP 4: Update Later{Style.RESET_ALL}
{Fore.CYAN}────────────────────────────────────────────────────────────────
cd ~/zisky-tg-ban
git pull origin main
python main.py
{Style.RESET_ALL}
""")
    
    input(f"\n{Fore.YELLOW}[Press Enter to return to main menu...]")

# ============================================================================
# TERMUX SETUP
# ============================================================================

def setup_termux():
    """Easy Termux setup"""
    print(f"{Fore.CYAN}{'═'*70}")
    print(f"{Fore.YELLOW}[🔧] ZISKY TG BAN - TERMUX SETUP")
    print(f"{Fore.CYAN}{'═'*70}")
    
    print(f"\n{Fore.GREEN}[1] Updating Termux...")
    os.system('pkg update -y && pkg upgrade -y')
    
    print(f"{Fore.GREEN}[2] Installing Python and dependencies...")
    os.system('pkg install python git clang libffi openssl -y')
    
    print(f"{Fore.GREEN}[3] Installing Python packages...")
    os.system('pip install requests colorama pysocks urllib3')
    
    print(f"{Fore.GREEN}[4] Creating proxy files...")
    open("Proxies.txt", 'w').close()
    open("https.txt", 'w').close()
    
    print(f"\n{Fore.GREEN}[✅] SETUP COMPLETE!")
    print(f"{Fore.YELLOW}[📁] Created:")
    print(f"  {Fore.CYAN}• Proxies.txt - Add your SOCKS5/HTTP proxies here")
    print(f"  {Fore.CYAN}• https.txt - Add your HTTPS proxies here")
    print(f"\n{Fore.YELLOW}[🚀] To run:")
    print(f"  {Fore.CYAN}python main.py")
    print(f"\n{Fore.YELLOW}[🐙] For GitHub setup, select option 4 in main menu")
    
    input(f"\n{Fore.YELLOW}[Press Enter to continue...]")

# ============================================================================
# MAIN
# ============================================================================

if __name__ == "__main__":
    try:
        if len(sys.argv) > 1:
            if sys.argv[1] == 'setup':
                setup_termux()
            else:
                print(f"{Fore.YELLOW}Usage: python main.py [setup]")
        else:
            tool = ZiskyTGBanTool()
            tool.run()
    except KeyboardInterrupt:
        print(f"\n{Fore.YELLOW}[⚠️] Interrupted by user")
    except Exception as e:
        print(f"\n{Fore.RED}[💥] Error: {e}")
        import traceback
        traceback.print_exc()
