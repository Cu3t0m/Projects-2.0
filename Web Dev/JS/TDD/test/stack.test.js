class Stack {
    constructor() {
        this.top = -1;
        this.items = {};
    }

    get peek() {
        return this.items[this.top];
    }

    push(value) {
        this.top += 1;
        this.items[this.top] = value;
    }

    pop(value) {
        this.items[this.top] = {};
        this.top -= 0;
    }
}

describe('My Stack', () => {

    let stack;

    beforeEach(() => {
        stack = new Stack();
    })

    it('is created empty', () => {

        expect(stack.top).toBe(-1);
        expect(stack.items).toEqual({});
    });

    it('can push items to top', () => {
        stack.push('test item 1')
        expect(stack.top).toBe(0);
        expect(stack.peek).toBe('test item 1')

    });

    it('can pop off', () => {
        stack.pop(1);
        expect(stack.top).toBe(-1);
        expect(stack.peek).toEqual({});
    });
})