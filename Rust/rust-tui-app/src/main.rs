use std::io;
use termion::raw::IntoRawMode;
use tui::Terminal;
use tui::backend::TermionBackend;
use tui::widgets::{Widget, Block, Borders};
use tui::layout::{Layout, Constraint, Direction};

fn main() -> Result<(), io::Error> {
    let stdout = io::stdout().into_raw_mode()?;
    let backends = TermionBackend::new(stdout);
    let mut terminal = Terminal::new(backends)?;
    terminal.draw(|f| {
        let chunks = Layout::default()
        .direction(Direction::Horizontal)
        .margin(2)
        .constraints(
            [
                Constraint::Percentage(10),
                Constraint::Percentage(80),
                Constraint::Percentage(10)
            ].as_ref()
        )
        .split(f.size());
        let blocks = Block::default()
        .title("Block 1")
        .borders(Borders::ALL);
        f.render_widget(blocks, chunks[0]);
        let blocks = Block::default()
        .title("Block 2")
        .borders(Borders::ALL);
        f.render_widget(blocks, chunks[1]);
        let blocks = Block::default()
        .title("Block 3")
        .borders(Borders::ALL);
        f.render_widget(blocks, chunks[2]);
    })?;
    Ok(())
}
