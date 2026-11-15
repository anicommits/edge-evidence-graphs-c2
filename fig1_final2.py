"""
fig1_final2.py
Generates clean, publication-quality, authentic IEEE-style technical diagram for:
- Figure 1: End-to-End SP-SP-GAT Architecture with Specified Deterministic Command Gate
All labels strictly synchronized with paper text. Minimum font size >= 7.0 pt.
Fixes all text overlaps:
- Header strip labels separated cleanly from top container borders
- "Feature Tensor & Evidence" label positioned cleanly between evidence and model box
- Command-gate box enlarged/repositioned so all 9 predicates and headers fit comfortably without overlapping borders
"""

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch
import os

# Styling configuration for IEEE Transactions / Conference style
plt.rcParams.update({
    'font.family': 'serif',
    'font.serif': ['Times New Roman', 'DejaVu Serif', 'Liberation Serif'],
    'mathtext.fontset': 'stix',
})

# Academic Research Palette
NAVY_DARK   = '#0B1D33'
NAVY_MED    = '#1A365D'
NAVY_LIGHT  = '#EBF4FF'
SLATE_DARK  = '#2D3748'
SLATE_LIGHT = '#F7FAFC'
AMBER_DARK  = '#7B341E'
AMBER_LIGHT = '#FFFAF0'
GREEN_DARK  = '#1C4532'
GREEN_LIGHT = '#F0FFF4'
RED_DARK    = '#742A2A'
RED_LIGHT   = '#FFF5F5'
PURPLE_DARK = '#44337A'
PURPLE_LIGHT = '#FAF5FF'
BORDER_GRAY = '#718096'
TEXT_BLACK  = '#1A202C'
TEXT_MUTED  = '#4A5568'

def draw_box(ax, xy, width, height, title, subtitle=None, details=None, 
             bg_color='#FFFFFF', border_color=BORDER_GRAY, border_width=1.1, 
             title_color=NAVY_DARK, title_size=8.5, sub_size=7.5, det_size=7.2,
             corner_radius=0.012, title_weight='bold'):
    """Draws a crisp rectangular box with header, subtitle, and bullet details."""
    x, y = xy
    box = FancyBboxPatch((x, y), width, height,
                         boxstyle=f"round,pad=0,rounding_size={corner_radius}",
                         facecolor=bg_color, edgecolor=border_color,
                         linewidth=border_width, zorder=2)
    ax.add_patch(box)
    
    if subtitle and details:
        ax.text(x + width/2.0, y + height - 0.022, title,
                ha='center', va='top', fontsize=title_size, fontweight=title_weight,
                color=title_color, zorder=3)
        ax.text(x + width/2.0, y + height - 0.052, subtitle,
                ha='center', va='top', fontsize=sub_size, style='italic',
                color=TEXT_MUTED, zorder=3)
        ax.text(x + width/2.0, y + (height - 0.055)/2.0 - 0.005, details,
                ha='center', va='center', fontsize=det_size,
                color=TEXT_BLACK, zorder=3, linespacing=1.2)
    elif subtitle:
        ax.text(x + width/2.0, y + height/2.0 + 0.016, title,
                ha='center', va='top', fontsize=title_size, fontweight=title_weight,
                color=title_color, zorder=3)
        ax.text(x + width/2.0, y + height/2.0 - 0.018, subtitle,
                ha='center', va='top', fontsize=sub_size,
                color=TEXT_MUTED, zorder=3)
    else:
        ax.text(x + width/2.0, y + height/2.0, title,
                ha='center', va='center', fontsize=title_size, fontweight=title_weight,
                color=title_color, zorder=3)
    return box

def draw_arrow(ax, start, end, label=None, label_pos='top', color=NAVY_MED, 
               lw=1.2, style='->', ls='-', label_size=7.2, label_color=NAVY_DARK,
               box_pad=0.12):
    """Draws a clean directional connecting arrow with label."""
    ax.annotate('', xy=end, xytext=start,
                arrowprops=dict(arrowstyle=style, color=color, lw=lw, ls=ls,
                                shrinkA=1, shrinkB=1), zorder=4)
    if label:
        mx = (start[0] + end[0]) / 2.0
        my = (start[1] + end[1]) / 2.0
        dy = 0.015 if label_pos == 'top' else -0.018
        ax.text(mx, my + dy, label, ha='center', va='center',
                fontsize=label_size, fontweight='bold', color=label_color,
                bbox=dict(boxstyle=f'square,pad={box_pad}', facecolor='#FFFFFF', edgecolor='none', alpha=0.92),
                zorder=5)

def generate_figure_1():
    fig, ax = plt.subplots(figsize=(10.5, 5.8), dpi=300)
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis('off')

    # Domain Container 1: Ground Identity & Command Domain
    ground_box = FancyBboxPatch((0.02, 0.48), 0.37, 0.49,
                                boxstyle="round,pad=0.01,rounding_size=0.012",
                                facecolor=SLATE_LIGHT, edgecolor=BORDER_GRAY, lw=1.0, ls='--')
    ax.add_patch(ground_box)
    ax.text(0.035, 0.945, 'GROUND IDENTITY & COMMAND DOMAIN', fontsize=8.5, fontweight='bold', color=NAVY_DARK)
    ax.text(0.035, 0.922, 'Independent enterprise credentials and cryptographic signing', fontsize=7.2, style='italic', color=TEXT_MUTED)

    # Nodes in Ground Domain
    draw_box(ax, (0.035, 0.73), 0.16, 0.16, 'Operator', 'Human Principal', 'FIDO2 / PIV / MFA\nRole & Shift Context', bg_color='#FFFFFF', border_color=NAVY_MED, det_size=7.0)
    draw_box(ax, (0.215, 0.73), 0.16, 0.16, 'Workstation', 'Ground Endpoint', 'TPM / Device Cert\nSecure Boot Attest', bg_color='#FFFFFF', border_color=NAVY_MED, det_size=7.0)
    draw_box(ax, (0.035, 0.51), 0.16, 0.17, 'IAM / Policy PDP', 'Access Control', 'Target & Opcode Scope\nDual-Approval Token', bg_color='#FFFFFF', border_color=NAVY_MED, det_size=7.0)
    draw_box(ax, (0.215, 0.51), 0.16, 0.17, 'Signer / HSM', 'Cryptographic Entity', 'Signed Command Hash\nKey Epoch & Nonce', bg_color='#FFFFFF', border_color=NAVY_MED, det_size=7.0)

    # Arrows in Ground Domain
    draw_arrow(ax, (0.195, 0.81), (0.215, 0.81), 'OPERATES', label_pos='top')
    draw_arrow(ax, (0.115, 0.73), (0.115, 0.68), 'AUTHENTICATES', label_pos='top')
    draw_arrow(ax, (0.195, 0.595), (0.215, 0.595), 'AUTHORIZES', label_pos='top')

    # Domain Container 2: Contested Space Link & Gateway Domain
    link_box = FancyBboxPatch((0.41, 0.48), 0.23, 0.49,
                              boxstyle="round,pad=0.01,rounding_size=0.012",
                              facecolor=AMBER_LIGHT, edgecolor=AMBER_DARK, lw=1.0, ls='--')
    ax.add_patch(link_box)
    ax.text(0.425, 0.945, 'CONTESTED SPACE LINK', fontsize=8.5, fontweight='bold', color=AMBER_DARK)
    ax.text(0.425, 0.922, 'Protocol termination & re-origination', fontsize=7.2, style='italic', color=TEXT_MUTED)

    draw_box(ax, (0.425, 0.73), 0.20, 0.16, 'TT&C Ground Gateway', 'Ground Protocol PEP', 'TLS 1.3 Endpoint\nFrame Multiplexer', bg_color='#FFFFFF', border_color=AMBER_DARK, det_size=7.0)
    draw_box(ax, (0.425, 0.51), 0.20, 0.17, 'CCSDS Space Link', 'RF Uplink & Downlink', 'CCSDS 355.0 SDLS\nSA, Counter, Anti-Replay', bg_color='#FFFFFF', border_color=AMBER_DARK, det_size=7.0)

    draw_arrow(ax, (0.375, 0.595), (0.425, 0.78), 'RELEASES', color=NAVY_MED)
    draw_arrow(ax, (0.525, 0.73), (0.525, 0.68), 'ENCAPSULATES', color=AMBER_DARK)

    # Domain Container 3: Spacecraft Subsystem Trust Domains
    space_box = FancyBboxPatch((0.66, 0.48), 0.32, 0.49,
                               boxstyle="round,pad=0.01,rounding_size=0.012",
                               facecolor=GREEN_LIGHT, edgecolor=GREEN_DARK, lw=1.0, ls='--')
    ax.add_patch(space_box)
    ax.text(0.675, 0.945, 'SPACECRAFT TRUST DOMAINS', fontsize=8.5, fontweight='bold', color=GREEN_DARK)
    ax.text(0.675, 0.922, 'Onboard bus routing & physical actuation boundaries', fontsize=7.2, style='italic', color=TEXT_MUTED)

    draw_box(ax, (0.675, 0.73), 0.135, 0.16, 'Transponder / RX', 'Spacecraft Ingress', 'RF Demod / SDLS\nAnti-Replay Gate', bg_color='#FFFFFF', border_color=GREEN_DARK, det_size=7.0)
    draw_box(ax, (0.83, 0.73), 0.135, 0.16, 'C&DH Router', 'Flight Computer', 'Command Dispatch\nOnboard Bus PEP', bg_color='#FFFFFF', border_color=GREEN_DARK, det_size=7.0)

    draw_box(ax, (0.675, 0.51), 0.095, 0.17, 'EPS Subsystem', 'Power / Energy', 'Battery SoC\nArray Slew', bg_color='#FFFFFF', border_color=GREEN_DARK, title_size=7.5, sub_size=7.0, det_size=7.0)
    draw_box(ax, (0.775, 0.51), 0.095, 0.17, 'ADCS / GNC', 'Attitude Control', 'Reaction Wheel\nThruster Gate', bg_color='#FFFFFF', border_color=GREEN_DARK, title_size=7.5, sub_size=7.0, det_size=7.0)
    draw_box(ax, (0.875, 0.51), 0.095, 0.17, 'Relay / TM', 'Communications', 'Payload Route\nDownlink Buffer', bg_color='#FFFFFF', border_color=GREEN_DARK, title_size=7.5, sub_size=7.0, det_size=7.0)

    draw_arrow(ax, (0.625, 0.595), (0.675, 0.78), 'UPLINKS (RF)', color=AMBER_DARK)
    draw_arrow(ax, (0.81, 0.81), (0.83, 0.81), 'DELIVERS', color=GREEN_DARK)
    draw_arrow(ax, (0.87, 0.73), (0.72, 0.68), 'DISPATCHES', color=GREEN_DARK)
    draw_arrow(ax, (0.897, 0.73), (0.82, 0.68), '', color=GREEN_DARK)
    draw_arrow(ax, (0.925, 0.73), (0.92, 0.68), '', color=GREEN_DARK)

    # Lower Tier: Observation, Learning Plane, and Safety Shield
    lower_box = FancyBboxPatch((0.02, 0.025), 0.96, 0.415,
                               boxstyle="round,pad=0.01,rounding_size=0.012",
                               facecolor='#FAFBFC', edgecolor=BORDER_GRAY, lw=1.2)
    ax.add_patch(lower_box)
    ax.text(0.035, 0.41, 'OBSERVATION, RELATIONAL LEARNING & RUNTIME ASSURANCE ARCHITECTURE', fontsize=8.8, fontweight='bold', color=NAVY_DARK)

    # Ingested Evidence Blocks (clean spacing, x goes 0.035 to 0.46)
    draw_box(ax, (0.035, 0.16), 0.08, 0.22, 'Identity', 'Principal / MFA', 'Operator binding\nRole/Shift checks', bg_color='#FFFFFF', border_color=BORDER_GRAY, title_size=7.8, sub_size=7.0, det_size=7.0)
    draw_box(ax, (0.120, 0.16), 0.08, 0.22, 'Session', 'TLS 1.3 / mTLS', 'Cipher suites\nEndpoint posture', bg_color='#FFFFFF', border_color=BORDER_GRAY, title_size=7.8, sub_size=7.0, det_size=7.0)
    draw_box(ax, (0.205, 0.16), 0.08, 0.22, 'Space Link', 'CCSDS SDLS', 'Carrier SNR / BER\nAnti-replay window', bg_color='#FFFFFF', border_color=BORDER_GRAY, title_size=7.8, sub_size=7.0, det_size=7.0)
    draw_box(ax, (0.290, 0.16), 0.08, 0.22, 'Command', 'Signed Envelope', 'Opcode scope\nDual-approvals', bg_color='#FFFFFF', border_color=BORDER_GRAY, title_size=7.8, sub_size=7.0, det_size=7.0)
    draw_box(ax, (0.375, 0.16), 0.08, 0.22, 'Physical', 'State & Bounds', 'Battery SoC, slew\nCross-sensor data', bg_color='#FFFFFF', border_color=BORDER_GRAY, title_size=7.8, sub_size=7.0, det_size=7.0)

    # Connect top domains to lower evidence blocks
    draw_arrow(ax, (0.115, 0.48), (0.075, 0.38), 'telemetry', color=BORDER_GRAY, ls=':')
    draw_arrow(ax, (0.525, 0.48), (0.245, 0.38), 'telemetry', color=BORDER_GRAY, ls=':')
    draw_arrow(ax, (0.82, 0.48), (0.415, 0.38), 'telemetry', color=BORDER_GRAY, ls=':')

    # Arrow from Evidence Blocks to Relational SP-SP-GAT (ample span from 0.455 to 0.505)
    draw_arrow(ax, (0.455, 0.27), (0.505, 0.27), 'Feature Tensor\n& Evidence', label_pos='top', color=NAVY_MED, label_size=7.0, box_pad=0.1)

    # Learning Plane: Relational SP-SP-GAT box (x=0.505, width=0.21, height=0.235)
    draw_box(ax, (0.505, 0.145), 0.21, 0.235, 'Relational SP-SP-GAT', 'Edge-Aware Message Passing', 
             '• Relational Message Passing\n• Multi-Head Additive Attention\n• 18-Class Attack Classification\n• Relational Edge Risk Localization', 
             bg_color=PURPLE_LIGHT, border_color=PURPLE_DARK, title_color=PURPLE_DARK, title_size=8.2, sub_size=7.2, det_size=7.0)

    # Arrow from SP-SP-GAT to Command Gate (span from 0.715 to 0.755)
    draw_arrow(ax, (0.715, 0.27), (0.755, 0.27), 'Attack Risk &\nAction Rank', label_pos='top', color=PURPLE_DARK, label_size=7.0, box_pad=0.1)

    # Runtime Assurance Command Gate (x=0.755, width=0.215, height=0.235)
    # Specified - 9 Predicates in 4 Groups: All text neatly formatted and >= 7.0 pt
    cmd_gate_details = '• Auth (4): AuthUser, AuthDevice,\n  RoleAllows, ApprovalsPresent\n• Fresh (1): Fresh\n• Crypto/Route (3): PeerValid,\n  SignatureValid, CorrectRoute\n• Safe-State (1): StateSafe'
    draw_box(ax, (0.755, 0.145), 0.215, 0.235, 'Deterministic Command Gate', 'Specification Only (Not Implemented)', 
             cmd_gate_details,
             bg_color=RED_LIGHT, border_color=RED_DARK, title_color=RED_DARK, title_size=8.2, sub_size=7.0, det_size=7.0)

    # Bottom Invariant Note (x=0.035, y=0.065 and 0.04)
    ax.text(0.035, 0.065, r'FAIL-CLOSED COMMAND INVARIANT (SPECIFIED DESIGN): $\Phi = \bigwedge_{p \in \mathcal{P}} p(c)$ (9 predicates in 4 groups: authorization, freshness, crypto/integrity, safe-state).',
            fontsize=7.2, fontweight='bold', color=RED_DARK)
    ax.text(0.035, 0.040, 'Deterministic gate designed to be non-bypassable; enforcement not evaluated in this paper. A learned model cannot override failed predicates.',
            fontsize=7.0, style='italic', color=TEXT_BLACK)

    plt.tight_layout()
    plt.savefig('Fig1_final2.png', dpi=300, bbox_inches='tight')
    plt.savefig('Fig1_final2.pdf', bbox_inches='tight')
    plt.close()
    print("[+] Fig 1 final2 cleanly generated: Fig1_final2.png and Fig1_final2.pdf")

if __name__ == '__main__':
    generate_figure_1()
