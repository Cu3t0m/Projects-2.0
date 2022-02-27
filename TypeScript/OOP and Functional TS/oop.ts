// Object Oriented

class Emoji {
  private _prev;

  constructor(private _icon: string) {}

  get icon() {
    return this._icon;
  }

  get prev() {
    return this._prev;
  }

  change(val) {
    this._prev = this._icon;
    this._icon = val;
  }

  // Static Method
  static AddOneTo(val) {
    return 1 + val;
  }
}

const emoji = new Emoji("☀️");
console.log(emoji.icon, emoji.prev);

emoji.change("⚡️");
emoji.change("🍔");

console.log(emoji.icon, emoji.prev);

Emoji.AddOneTo(3);
