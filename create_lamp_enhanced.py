#!/usr/bin/env python3
"""
Create a high-quality realistic vintage lamp image for night-light web project.
Resolution: 512x512 pixels with transparent background.
"""

from PIL import Image, ImageDraw, ImageFilter, ImageEnhance
import math
import random
from io import BytesIO
import base64

def draw_elliptical_gradient(draw, bbox, inner_color, outer_color, vertical=True):
    """Draw an elliptical gradient."""
    x0, y0, x1, y1 = bbox
    width = x1 - x0
    height = y1 - y0
    center_x, center_y = (x0 + x1) / 2, (y0 + y1) / 2

    for i in range(height if vertical else width):
        ratio = i / (height if vertical else width)
        r = int(inner_color[0] * (1 - ratio) + outer_color[0] * ratio)
        g = int(inner_color[1] * (1 - ratio) + outer_color[1] * ratio)
        b = int(inner_color[2] * (1 - ratio) + outer_color[2] * ratio)

        if vertical:
            draw.rectangle([x0, y0 + i, x1, y0 + i + 1], fill=(r, g, b))
        else:
            draw.rectangle([x0 + i, y0, x0 + i + 1, y1], fill=(r, g, b))

def draw_cylindrical_surface(draw, bbox, color_light, color_dark, shadow_side='left'):
    """Draw a cylindrical surface with realistic lighting."""
    x0, y0, x1, y1 = bbox
    width = x1 - x0
    height = y1 - y0

    for y in range(y0, y1):
        for x in range(x0, x1):
            # Calculate normalized position
            if shadow_side == 'left':
                highlight = 0.3 + 0.7 * (x - x0) / width
            else:
                highlight = 0.3 + 0.7 * (x1 - x) / width

            # Add specular highlight effect
            if shadow_side == 'left' and (x - x0) / width > 0.65:
                highlight += 0.2 * ((x - x0) / width - 0.65) / 0.35
            elif shadow_side == 'right' and (x1 - x) / width > 0.65:
                highlight += 0.2 * ((x1 - x) / width - 0.65) / 0.35

            highlight = min(1.0, highlight)

            r = int(color_dark[0] + (color_light[0] - color_dark[0]) * highlight)
            g = int(color_dark[1] + (color_light[1] - color_dark[1]) * highlight)
            b = int(color_dark[2] + (color_light[2] - color_dark[2]) * highlight)

            draw.point((x, y), fill=(r, g, b, 255))

def draw_radial_glow(draw, center, radius, color, max_alpha=60):
    """Draw a radial glow effect."""
    cx, cy = center
    for r in range(radius, 0, -2):
        alpha = int(max_alpha * (1 - (r / radius) ** 2))
        draw.ellipse([
            cx - r, cy - r,
            cx + r, cy + r
        ], fill=(color[0], color[1], color[2], alpha))

def create_vintage_lamp():
    """Create a realistic vintage lamp at 512x512 resolution."""

    size = 512
    img = Image.new('RGBA', (size, size), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)

    center_x = size // 2
    stem_center_x = center_x

    # ===== COLOR PALETTE =====
    # Brass/Metal colors
    brass_light = (255, 225, 140)
    brass_medium = (218, 165, 32)
    brass_dark = (160, 110, 40)
    brass_shadow = (120, 80, 20)
    brass_highlight = (255, 245, 200)

    # Copper accents
    copper_light = (210, 140, 70)
    copper_dark = (140, 90, 40)

    # Glass colors
    glass_light = (255, 250, 240)
    glass_medium = (245, 235, 220)
    glass_dark = (220, 200, 180)

    # Bulb colors
    bulb_warm = (255, 248, 230)
    bulb_glow = (255, 240, 200)

    # ===== LAMP BASE =====
    base_bottom_y = 490
    base_top_y = 435
    base_width_bottom = 150
    base_width_top = 125

    # Ground shadow
    shadow_img = Image.new('RGBA', (size, size), (0, 0, 0, 0))
    shadow_draw = ImageDraw.Draw(shadow_img)
    for r in range(50, 0, -2):
        alpha = int(35 * (1 - r / 50))
        shadow_draw.ellipse([
            center_x - base_width_bottom//2 - 10,
            base_bottom_y,
            center_x + base_width_bottom//2 + 10,
            base_bottom_y + r * 0.4
        ], fill=(0, 0, 0, alpha))
    img = Image.alpha_composite(img, shadow_img)

    # Base bottom plate (largest)
    for y in range(20):
        y_pos = base_bottom_y - y
        progress = y / 20
        current_width = base_width_bottom * (1 - progress * 0.15)

        for x in range(int(current_width)):
            pos = x / current_width
            if pos < 0.5:
                intensity = 0.25 + 0.25 * (pos / 0.5)
            else:
                intensity = 0.5 + 0.5 * ((pos - 0.5) / 0.5)

            r = int(brass_shadow[0] + (brass_medium[0] - brass_shadow[0]) * intensity)
            g = int(brass_shadow[1] + (brass_medium[1] - brass_shadow[1]) * intensity)
            b = int(brass_shadow[2] + (brass_medium[2] - brass_shadow[2]) * intensity)

            draw.point((center_x - current_width//2 + x, y_pos), fill=(r, g, b, 255))

    # Base main body
    base_height = base_bottom_y - base_top_y - 20
    for y in range(base_top_y, base_bottom_y - 20):
        progress = (base_bottom_y - 20 - y) / base_height
        current_width = base_width_top + (base_width_bottom - base_width_top - 10) * progress

        for x in range(int(current_width)):
            pos = x / current_width
            if pos < 0.4:
                intensity = 0.3 + 0.2 * (pos / 0.4)
            elif pos < 0.7:
                intensity = 0.5 + 0.3 * ((pos - 0.4) / 0.3)
            else:
                intensity = 0.8 + 0.2 * ((pos - 0.7) / 0.3)

            r = int(brass_shadow[0] + (brass_highlight[0] - brass_shadow[0]) * intensity)
            g = int(brass_shadow[1] + (brass_highlight[1] - brass_shadow[1]) * intensity)
            b = int(brass_shadow[2] + (brass_highlight[2] - brass_shadow[2]) * intensity)

            draw.point((center_x - current_width//2 + x, y), fill=(r, g, b, 255))

    # Base top rim
    for i in range(15):
        y = base_top_y - i
        progress = i / 15
        intensity = 0.6 + 0.4 * progress
        current_width = base_width_top * (1 - i * 0.01)

        r = int(brass_dark[0] + (brass_highlight[0] - brass_dark[0]) * intensity)
        g = int(brass_dark[1] + (brass_highlight[1] - brass_dark[1]) * intensity)
        b = int(brass_dark[2] + (brass_highlight[2] - brass_dark[2]) * intensity)

        draw.ellipse([
            center_x - current_width,
            y - 5,
            center_x + current_width,
            y + 5
        ], fill=(r, g, b, 255))

    # Decorative rings on base
    ring_y_positions = [base_top_y + 25, base_top_y + 50]
    for ring_y in ring_y_positions:
        for i in range(8):
            y = ring_y - i
            progress = i / 8
            intensity = 0.5 + 0.5 * progress
            ring_width = base_width_top * (0.85 + i * 0.02)

            r = int(copper_dark[0] + (copper_light[0] - copper_dark[0]) * intensity)
            g = int(copper_dark[1] + (copper_light[1] - copper_dark[1]) * intensity)
            b = int(copper_dark[2] + (copper_light[2] - copper_dark[2]) * intensity)

            draw.ellipse([
                center_x - ring_width,
                y - 3,
                center_x + ring_width,
                y + 3
            ], fill=(r, g, b, 255))

    # ===== STEM/POLE =====
    stem_top_y = 330
    stem_bottom_y = base_top_y - 10
    stem_width_top = 22
    stem_width_bottom = 35

    for y in range(stem_bottom_y, stem_top_y, -1):
        progress = (stem_bottom_y - y) / (stem_bottom_y - stem_top_y)
        current_width = stem_width_bottom - (stem_width_bottom - stem_width_top) * progress

        # Subtle curve
        curve_offset = -12 * math.sin(progress * math.pi)
        stem_center_x = center_x + curve_offset

        for x in range(int(current_width)):
            pos = x / current_width

            if pos > 0.65:
                intensity = 0.85 + 0.15 * ((pos - 0.65) / 0.35)
            elif pos > 0.5:
                intensity = 0.6 + 0.25 * ((pos - 0.5) / 0.15)
            else:
                intensity = 0.3 + 0.3 * (pos / 0.5)

            r = int(brass_shadow[0] + (brass_highlight[0] - brass_shadow[0]) * intensity)
            g = int(brass_shadow[1] + (brass_highlight[1] - brass_shadow[1]) * intensity)
            b = int(brass_shadow[2] + (brass_highlight[2] - brass_shadow[2]) * intensity)

            draw.point((stem_center_x - current_width//2 + x, y), fill=(r, g, b, 255))

    # Stem decorative rings (copper)
    stem_rings_y = [stem_bottom_y - 45, stem_bottom_y - 85]
    for ring_y in stem_rings_y:
        for i in range(10):
            y = ring_y - i
            progress = i / 10
            intensity = 0.5 + 0.5 * progress
            ring_width = 26 + i * 0.3

            r = int(copper_dark[0] + (copper_light[0] - copper_dark[0]) * intensity)
            g = int(copper_dark[1] + (copper_light[1] - copper_dark[1]) * intensity)
            b = int(copper_dark[2] + (copper_light[2] - copper_dark[2]) * intensity)

            draw.ellipse([
                stem_center_x - max(ring_width, 1),
                y - 2,
                stem_center_x + max(ring_width, 1),
                y + 2
            ], fill=(r, g, b, 255))

    # ===== LAMP HOLDER NECK =====
    holder_y = stem_top_y
    holder_height = 65
    holder_width_top = 65
    holder_width_bottom = 40

    for y in range(holder_y, holder_y + holder_height):
        progress = (y - holder_y) / holder_height
        current_width = holder_width_bottom + (holder_width_top - holder_width_bottom) * progress

        for x in range(int(current_width)):
            pos = x / current_width

            if pos > 0.6:
                intensity = 0.7 + 0.3 * ((pos - 0.6) / 0.4)
            else:
                intensity = 0.35 + 0.35 * (pos / 0.6)

            r = int(brass_shadow[0] + (brass_light[0] - brass_shadow[0]) * intensity)
            g = int(brass_shadow[1] + (brass_light[1] - brass_shadow[1]) * intensity)
            b = int(brass_shadow[2] + (brass_light[2] - brass_shadow[2]) * intensity)

            draw.point((stem_center_x - current_width//2 + x, y), fill=(r, g, b, 255))

    # Finial on top
    finial_center_y = holder_y
    finial_radius = 18

    for angle in range(180):
        rad = math.radians(angle)
        y = finial_center_y - finial_radius + math.sin(rad) * finial_radius * 1.2
        width = math.cos(rad) * finial_radius
        intensity = 0.4 + 0.6 * math.sin(rad)

        r = int(brass_shadow[0] + (brass_highlight[0] - brass_shadow[0]) * intensity)
        g = int(brass_shadow[1] + (brass_highlight[1] - brass_shadow[1]) * intensity)
        b = int(brass_shadow[2] + (brass_highlight[2] - brass_shadow[2]) * intensity)

        draw.ellipse([
            stem_center_x - width,
            y - 3,
            stem_center_x + width,
            y + 3
        ], fill=(r, g, b, 255))

    # ===== GLASS SHADE =====
    shade_top_y = holder_y + holder_height - 25
    shade_bottom_y = 180
    shade_top_width = 95
    shade_bottom_width = 170

    # Back layer of glass
    for y in range(shade_top_y, shade_bottom_y, -1):
        progress = (shade_top_y - y) / (shade_top_y - shade_bottom_y)
        current_width = shade_top_width + (shade_bottom_width - shade_top_width) * progress

        # Glass transparency - more opaque at bottom
        alpha = int(180 + 75 * progress)

        for x in range(int(current_width)):
            pos = x / current_width

            if pos > 0.6:
                base_intensity = 0.85
            elif pos > 0.35:
                base_intensity = 0.65
            else:
                base_intensity = 0.45

            # Warm glow increases toward bottom
            glow_factor = 0.35 + 0.65 * progress

            r = min(255, int(glass_medium[0] * base_intensity * glow_factor))
            g = min(255, int(glass_medium[1] * base_intensity * glow_factor))
            b = min(255, int(glass_medium[2] * base_intensity * glow_factor))

            draw.point((stem_center_x - current_width//2 + x, y), fill=(r, g, b, alpha))

    # Glass reflections
    for y in range(shade_top_y + 15, shade_bottom_y - 15):
        progress = (y - shade_top_y) / (shade_bottom_y - shade_top_y)
        current_width = shade_top_width + (shade_bottom_width - shade_top_width) * progress

        # Main highlight on right
        highlight_x = stem_center_x + current_width * 0.28
        highlight_width = 4

        for i in range(highlight_width):
            alpha = int(120 * (1 - abs(i - 1.5) / highlight_width))
            draw.point((int(highlight_x + i - 1.5), y), fill=(255, 255, 255, alpha))

        # Secondary highlight on left
        highlight_x2 = stem_center_x - current_width * 0.2
        highlight_width2 = 2

        for i in range(highlight_width2):
            alpha = int(60 * (1 - abs(i - 0.5) / highlight_width2))
            draw.point((int(highlight_x2 + i - 0.5), y), fill=(255, 255, 255, alpha))

    # Shade rim (brass ring)
    rim_height = 12
    for i in range(rim_height):
        y = shade_bottom_y + i - 6
        progress = i / rim_height
        intensity = 0.6 + 0.4 * progress
        rim_width = shade_bottom_width + i * 1.5

        r = int(brass_dark[0] + (brass_light[0] - brass_dark[0]) * intensity)
        g = int(brass_dark[1] + (brass_light[1] - brass_dark[1]) * intensity)
        b = int(brass_dark[2] + (brass_light[2] - brass_dark[2]) * intensity)

        draw.ellipse([
            stem_center_x - rim_width,
            y - 3,
            stem_center_x + rim_width,
            y + 3
        ], fill=(r, g, b, 255))

    # ===== BULB INSIDE =====
    bulb_center_y = shade_bottom_y + 25
    bulb_radius = 28

    # Create separate layer for bulb glow
    bulb_layer = Image.new('RGBA', (size, size), (0, 0, 0, 0))
    bulb_draw = ImageDraw.Draw(bulb_layer)

    # Outer glow (warm light)
    draw_radial_glow(bulb_draw, (stem_center_x, bulb_center_y), bulb_radius + 50, (255, 240, 210), 40)

    # Bulb glass body
    for angle in range(180):
        rad = math.radians(angle)
        bulb_top = bulb_center_y - bulb_radius * 1.5
        bulb_width = math.cos(rad) * bulb_radius
        y = bulb_top + math.sin(rad) * bulb_radius * 1.5

        intensity = 0.75 + 0.25 * math.sin(rad)

        r = int(bulb_warm[0] * intensity)
        g = int(bulb_warm[1] * intensity)
        b = int(bulb_warm[2] * intensity)

        bulb_draw.ellipse([
            stem_center_x - bulb_width,
            y - 3,
            stem_center_x + bulb_width,
            y + 3
        ], fill=(r, g, b, 255))

    # Bulb filament glow
    filament_y = bulb_center_y - 10
    filament_radius = 12
    draw_radial_glow(bulb_draw, (stem_center_x, filament_y), filament_radius, (255, 255, 220), 80)

    # Bulb socket/metal base
    socket_y = int(bulb_center_y - bulb_radius * 1.5)
    socket_width = 22
    socket_height = 18

    for y in range(socket_y, socket_y + socket_height):
        for x in range(socket_width):
            pos = x / socket_width
            intensity = 0.3 + 0.7 * pos

            r = int(brass_shadow[0] * intensity)
            g = int(brass_shadow[1] * intensity)
            b = int(brass_shadow[2] * intensity)

            bulb_draw.point((stem_center_x - socket_width//2 + x, y), fill=(r, g, b, 255))

    # Socket threading
    for i in range(6):
        y = socket_y - i * 3
        thread_color = brass_dark if i % 2 == 0 else brass_shadow
        bulb_draw.ellipse([
            stem_center_x - socket_width//2 - 2,
            y - 1,
            stem_center_x + socket_width//2 + 2,
            y + 1
        ], fill=thread_color)

    img = Image.alpha_composite(img, bulb_layer)

    # ===== PULL CHAIN =====
    chain_start_y = holder_y + 40
    chain_base_x = stem_center_x + 45
    chain_length = 90

    # Chain cord with curve
    for y in range(chain_start_y, chain_start_y + chain_length):
        progress = (y - chain_start_y) / chain_length
        curve = 10 * math.sin(progress * math.pi * 0.7)
        chain_x = chain_base_x + curve

        # Link pattern
        link_num = int((y - chain_start_y) // 7)
        if link_num % 2 == 0:
            color = brass_medium
        else:
            color = brass_light

        draw.ellipse([
            chain_x - 2,
            y,
            chain_x + 2,
            y + 4
        ], fill=color)

    # Chain pull handle
    pull_y = chain_start_y + chain_length + 15
    pull_radius = 10

    for angle in range(180):
        rad = math.radians(angle)
        y = pull_y - pull_radius + math.sin(rad) * pull_radius * 1.3
        width = math.cos(rad) * pull_radius
        intensity = 0.4 + 0.6 * math.sin(rad)

        r = int(brass_shadow[0] + (brass_highlight[0] - brass_shadow[0]) * intensity)
        g = int(brass_shadow[1] + (brass_highlight[1] - brass_shadow[1]) * intensity)
        b = int(brass_shadow[2] + (brass_highlight[2] - brass_shadow[2]) * intensity)

        draw.ellipse([
            chain_base_x - width,
            y - 3,
            chain_base_x + width,
            y + 3
        ], fill=(r, g, b, 255))

    # ===== AMBIENT GLOW =====
    ambient_layer = Image.new('RGBA', (size, size), (0, 0, 0, 0))
    ambient_draw = ImageDraw.Draw(ambient_layer)

    # Warm ambient glow from shade
    ambient_center_y = shade_bottom_y + 60
    for r in range(120, 0, -4):
        alpha = int(20 * (1 - (r / 120) ** 1.5))
        ambient_draw.ellipse([
            center_x - r * 0.7,
            ambient_center_y - r,
            center_x + r * 0.7,
            ambient_center_y + r * 0.35
        ], fill=(255, 230, 190, alpha))

    img = Image.alpha_composite(img, ambient_layer)

    # ===== FINAL POLISH =====
    # Very subtle blur for softness
    img = img.filter(ImageFilter.GaussianBlur(radius=1))

    # Slight contrast enhancement
    enhancer = ImageEnhance.Contrast(img)
    img = enhancer.enhance(1.03)

    # Slight saturation boost
    color_enhancer = ImageEnhance.Color(img)
    img = color_enhancer.enhance(1.05)

    return img

def main():
    """Generate the vintage lamp image."""
    print("Creating high-quality vintage lamp (512x512)...")

    lamp = create_vintage_lamp()

    # Save as PNG with transparency
    output_path = '/Users/apple/Documents/opencode_lab/night-light/vintage-lamp.png'
    lamp.save(output_path, 'PNG', optimize=True)
    print(f"✓ Saved to: {output_path}")

    # Generate base64 encoding
    buffered = BytesIO()
    lamp.save(buffered, format="PNG", optimize=True)
    img_b64 = base64.b64encode(buffered.getvalue()).decode('utf-8')
    data_url = f"data:image/png;base64,{img_b64}"

    # Save base64 to file
    base64_path = '/Users/apple/Documents/opencode_lab/night-light/vintage-lamp-base64.txt'
    with open(base64_path, 'w') as f:
        f.write(f"<!-- Vintage Lamp Data URL (512x512) -->\n")
        f.write(f"<!-- Length: {len(img_b64)} characters -->\n\n")
        f.write(f"<!-- Use as img src: -->\n")
        f.write(f'<img src="{data_url}" alt="Vintage Lamp" class="lamp">\n\n')
        f.write(f"<!-- Use as background-image in CSS: -->\n")
        f.write(f"background-image: url({data_url});\n")
        f.write(f"background-size: contain;\n")
        f.write(f"background-repeat: no-repeat;\n")
        f.write(f"background-position: center;\n\n")
        f.write(f"<!-- Or as inline style: -->\n")
        f.write(f'style="background-image: url({data_url}); background-size: contain; background-repeat: no-repeat; background-position: center;"\n')

    print(f"✓ Base64 encoding saved to: {base64_path}")
    print(f"✓ Image dimensions: {lamp.size[0]}x{lamp.size[1]} pixels")
    print(f"✓ Image mode: {lamp.mode}")
    print(f"\nTo use in HTML:")
    print(f'  <img src="{data_url[:50]}..." alt="Vintage Lamp">')

    return lamp

if __name__ == '__main__':
    main()
