#!/usr/bin/env python3
"""
Crafted Radiance - Vintage Lamp Generator
Based on the Crafted Radiance design philosophy
"""

from PIL import Image, ImageDraw, ImageFilter, ImageEnhance
import math

def create_gradient(draw, bbox, color1, color2, direction='vertical'):
    """Create a gradient between two colors"""
    x0, y0, x1, y1 = bbox
    width = x1 - x0
    height = y1 - y0

    for i in range(height):
        ratio = i / height
        r = int(color1[0] * (1 - ratio) + color2[0] * ratio)
        g = int(color1[1] * (1 - ratio) + color2[1] * ratio)
        b = int(color1[2] * (1 - ratio) + color2[2] * ratio)
        draw.rectangle([x0, y0 + i, x1, y0 + i + 1], fill=(r, g, b))

def radial_glow(draw, center, radius, inner_color, outer_color):
    """Create radial glow effect"""
    for r in range(radius, 0, -1):
        ratio = r / radius
        # Exponential falloff for more realistic glow
        alpha = int(255 * (1 - ratio ** 2))
        if alpha < 0:
            alpha = 0
        color = (
            int(inner_color[0] * (1 - ratio) + outer_color[0] * ratio),
            int(inner_color[1] * (1 - ratio) + outer_color[1] * ratio),
            int(inner_color[2] * (1 - ratio) + outer_color[2] * ratio)
        )
        draw.ellipse([
            center[0] - r, center[1] - r,
            center[0] + r, center[1] + r
        ], fill=color)

def draw_bulb(draw, center, radius):
    """Draw vintage incandescent bulb"""
    cx, cy = center

    # Bulb glass - warm amber/yellow gradient
    bulb_color = (255, 248, 220)  # Cornsilk

    # Main bulb shape
    bulb_height = radius * 2.2
    bulb_width = radius * 1.6

    # Draw bulb base
    draw.ellipse([
        cx - bulb_width//2, cy - bulb_height//2,
        cx + bulb_width//2, cy + bulb_height//2
    ], fill=bulb_color)

    # Bulb socket/metal base
    socket_height = 15
    socket_width = bulb_width * 0.7
    draw.rectangle([
        cx - socket_width//2, cy + bulb_height//2,
        cx + socket_width//2, cy + bulb_height//2 + socket_height
    ], fill=(101, 67, 33))  # Dark brown

    # Socket threading details
    for i in range(3):
        y_pos = cy + bulb_height//2 + 3 + i * 4
        draw.line([
            cx - socket_width//2 + 2, y_pos,
            cx + socket_width//2 - 2, y_pos
        ], fill=(139, 90, 43), width=1)

    # Filament glow (subtle)
    filament_color = (255, 255, 200)
    draw.ellipse([
        cx - radius//3, cy - radius//3,
        cx + radius//3, cy + radius//3
    ], fill=filament_color)

    return bulb_width, bulb_height

def create_vintage_lamp():
    """Create a masterpiece vintage lamp following Crafted Radiance philosophy"""

    # Canvas size
    width, height = 200, 300

    # Create image with alpha channel (transparent background)
    img = Image.new('RGBA', (width, height), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)

    center_x = width // 2

    # ===== LAMP BASE =====
    # Brass base with patina
    base_y = 270
    base_width = 60
    base_height = 25

    # Main base - brass gradient (darker at bottom for depth)
    for y in range(base_height):
        ratio = y / base_height
        # Brass colors: from (255, 215, 0) to (184, 134, 11)
        r = int(255 - (255 - 184) * ratio)
        g = int(215 - (215 - 134) * ratio)
        b = int(0 + (11 - 0) * ratio)
        current_width = base_width * (1 - ratio * 0.3)  # Slightly narrower at bottom
        draw.rectangle([
            center_x - current_width//2, base_y - base_height + y,
            center_x + current_width//2, base_y - base_height + y + 1
        ], fill=(r, g, b))

    # Base edge highlight (brass reflection)
    draw.line([
        center_x - base_width//2, base_y - base_height,
        center_x + base_width//2, base_y - base_height
    ], fill=(255, 235, 150), width=2)

    # Base bottom shadow (for depth)
    shadow_img = Image.new('RGBA', (width, height), (0, 0, 0, 0))
    shadow_draw = ImageDraw.Draw(shadow_img)
    shadow_draw.ellipse([
        center_x - 45, base_y - 5,
        center_x + 45, base_y + 10
    ], fill=(0, 0, 0, 40))
    img = Image.alpha_composite(img, shadow_img)

    # ===== LAMP SHAFT =====
    # Metal shaft with aged patina
    shaft_top_y = 100
    shaft_bottom_y = 245
    shaft_width = 12

    # Main shaft - darkened brass/copper with patina
    for y in range(shaft_top_y, shaft_bottom_y):
        ratio = (y - shaft_top_y) / (shaft_bottom_y - shaft_top_y)

        # Copper/brass with oxidation (darker at top and bottom)
        # Base color: aged copper
        base_r, base_g, base_b = (139, 90, 43)  # SaddleBrown

        # Add subtle vertical gradient
        r = base_r - int(20 * math.sin(ratio * math.pi))
        g = base_g - int(15 * math.sin(ratio * math.pi))
        b = base_b - int(10 * math.sin(ratio * math.pi))

        draw.rectangle([
            center_x - shaft_width//2, y,
            center_x + shaft_width//2, y + 1
        ], fill=(r, g, b))

    # Shaft highlight (left edge) - brass reflection
    for y in range(shaft_top_y + 5, shaft_bottom_y - 5):
        highlight_alpha = int(80 * (1 - abs((y - (shaft_top_y + shaft_bottom_y) / 2) / 70)))
        if highlight_alpha > 0:
            draw.point((center_x - shaft_width//2 + 1, y), fill=(255, 220, 150, highlight_alpha))

    # ===== LAMP SHADE =====
    # Vintage glass shade - cone shape
    shade_top_y = 50
    shade_bottom_y = 95
    shade_top_width = 35
    shade_bottom_width = 70

    # Shade back layer (darker amber)
    shade_back_color = (205, 160, 80)  # Dark amber
    for y in range(shade_top_y, shade_bottom_y):
        ratio = (y - shade_top_y) / (shade_bottom_y - shade_top_y)
        current_width = shade_top_width + (shade_bottom_width - shade_top_width) * ratio
        draw.polygon([
            center_x - current_width//2, y,
            center_x + current_width//2, y,
            center_x + (shade_bottom_width - shade_top_width) // 2 + shade_top_width // 2, shade_bottom_y,
            center_x - (shade_bottom_width - shade_top_width) // 2 - shade_top_width // 2, shade_bottom_y
        ], fill=shade_back_color)

    # Shade rim (brass ring)
    rim_thickness = 3
    rim_color = (184, 134, 11)  # Dark gold
    draw.ellipse([
        center_x - shade_bottom_width//2 - rim_thickness, shade_bottom_y - 3,
        center_x + shade_bottom_width//2 + rim_thickness, shade_bottom_y + 3
    ], fill=rim_color)

    # Shade front highlight (glass reflection)
    highlight_poly = [
        (center_x - 8, shade_top_y + 5),
        (center_x + 8, shade_top_y + 5),
        (center_x + 12, shade_bottom_y - 10),
        (center_x - 12, shade_bottom_y - 10)
    ]
    draw.polygon(highlight_poly, fill=(255, 255, 230, 40))  # Subtle white highlight

    # ===== BULB INSIDE SHADE =====
    bulb_center = (center_x, shade_bottom_y - 15)
    bulb_radius = 12

    # Draw bulb
    draw_bulb(draw, bulb_center, bulb_radius)

    # ===== SHADE TOP CAP =====
    # Brass cap at top of shade
    cap_y = shade_top_y - 8
    cap_width = 40
    cap_height = 10

    # Cap gradient
    for y in range(cap_height):
        ratio = y / cap_height
        r = int(184 + (255 - 184) * (1 - ratio))
        g = int(134 + (215 - 134) * (1 - ratio))
        b = int(11 + (0 - 11) * (1 - ratio))
        draw.rectangle([
            center_x - cap_width//2, cap_y + y,
            center_x + cap_width//2, cap_y + y + 1
        ], fill=(r, g, b))

    # ===== JOINTS AND DETAILS =====
    # Base to shaft joint
    joint_y = shaft_bottom_y
    joint_width = 20
    joint_height = 6

    for y in range(joint_height):
        ratio = y / joint_height
        # Brass gradient
        r = int(184 + (139 - 184) * ratio)
        g = int(134 + (90 - 134) * ratio)
        b = int(11 + (43 - 11) * ratio)
        current_width = joint_width - (joint_width - shaft_width) * ratio
        draw.rectangle([
            center_x - current_width//2, joint_y + y,
            center_x + current_width//2, joint_y + y + 1
        ], fill=(r, g, b))

    # Shade to shaft joint
    shade_joint_y = shade_bottom_y + 2
    shade_joint_width = 18
    shade_joint_height = 8

    for y in range(shade_joint_height):
        ratio = y / shade_joint_height
        # Brass
        r = int(184 - (184 - 139) * ratio)
        g = int(134 - (134 - 90) * ratio)
        b = int(11 + (43 - 11) * ratio)
        current_width = shade_joint_width - (shade_joint_width - shaft_width) * (1 - ratio)
        draw.rectangle([
            center_x - current_width//2, shade_joint_y + y,
            center_x + current_width//2, shade_joint_y + y + 1
        ], fill=(r, g, b))

    # ===== SUBTLE PATINA AND WEAR =====
    # Add age marks and oxidation patterns
    patina_layer = Image.new('RGBA', (width, height), (0, 0, 0, 0))
    patina_draw = ImageDraw.Draw(patina_layer)

    # Subtle oxidation spots on base
    import random
    random.seed(42)  # For consistency

    for _ in range(15):
        px = center_x - base_width//2 + random.randint(0, base_width)
        py = base_y - base_height + random.randint(0, base_height)
        patina_draw.ellipse([
            px - 1, py - 1,
            px + 1, py + 1
        ], fill=(0, 0, 0, 30))

    # Shaft oxidation streak
    for _ in range(20):
        px = center_x - shaft_width//2 + random.randint(0, shaft_width)
        py = shaft_top_y + random.randint(0, shaft_bottom_y - shaft_top_y)
        patina_draw.rectangle([
            px, py,
            px + 1, py + 2
        ], fill=(0, 0, 0, 20))

    img = Image.alpha_composite(img, patina_layer)

    # ===== FINAL POLISH =====
    # Apply subtle blur to soften edges (vintage effect)
    # Only blur slightly to maintain crispness
    img = img.filter(ImageFilter.GaussianBlur(radius=0.3))

    # Enhance contrast slightly for depth
    enhancer = ImageEnhance.Contrast(img)
    img = enhancer.enhance(1.05)

    # Enhance color saturation slightly
    color_enhancer = ImageEnhance.Color(img)
    img = color_enhancer.enhance(1.1)

    return img

def main():
    """Generate the vintage lamp image"""
    print("Creating Crafted Radiance vintage lamp...")

    lamp = create_vintage_lamp()

    # Save as PNG with transparency
    output_path = 'vintage-lamp.png'
    lamp.save(output_path, 'PNG', optimize=True)
    print(f"Saved to: {output_path}")

    # Generate base64 encoding
    import base64
    import io

    buffered = io.BytesIO()
    lamp.save(buffered, format="PNG", optimize=True)
    img_str = base64.b64encode(buffered.getvalue()).decode()

    # Save base64 to file
    with open('vintage-lamp-base64.txt', 'w') as f:
        f.write(f"data:image/png;base64,{img_str}")

    print("Base64 encoding saved to: vintage-lamp-base64.txt")

    return lamp

if __name__ == '__main__':
    main()
