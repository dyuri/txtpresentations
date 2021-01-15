registerPaint('demoCircle', class DemoCircle {
  static get contextOptions() {
    return {alpha: true};
  }

  static getColor(width) {
    if (width > 360) {
      return 'rgba(205, 220, 57, .8)';
    }
    return `hsla(${width}, 90%, 60%, .9)`;
  }

  paint(ctx, size) {
    const offset = 10;
    const r = Math.min(size.width, size.height) / 4 - offset;
    const cx = size.width - offset - r;
    const cy = offset + r;

    if (r > 0) {
      ctx.fillStyle = DemoCircle.getColor(size.width);
      ctx.beginPath();
      ctx.arc(cx, cy, r, 0, 2 * Math.PI);
      ctx.fill();
    }
  }
});

registerPaint('headerHighlight', class {

  static get contextOptions() {
    return { alpha: true };
  }

  static get inputProperties() {
    return ['--hlColor'];
  }

  static get inputArguments() {
    return ['<number>'];
  }

  paint(ctx, size, props, args) {
    let color = props.get('--hlColor');
    let width = +args[0] || size.width / 2;
    if (!color.length) {
      color = 'hsla(55, 90%, 60%, 1.0)';
    }
    ctx.fillStyle = color;
    ctx.fillRect(0, size.height / 3, width, size.height * .6);  /* order: x, y, w, h */
  }
});

