confused <- c(4.571555420127652, 4.247821300948029)
afraid <- c(1.8066831304229474, 2.3991582063920314)
scared <- c(0.6923256853908628, 2.3392476965292524)

colors <- c("blue", "green", "blue", "green", "blue", "green")

barplot(cbind(confused, afraid, scared), beside = TRUE, names.arg = c("confused", "afraid", "scared"), col = colors, ylim = c(0,5), main = "Mean quality of the Pacman belief state", ylab = "Mean quality")
legend("topright", legend = c("large_filter layout", "large_filter_walls layout"), col=c("blue", "green"), pch = c(15,15))

text(1.5, 0.4,round(4.571555420127652, digits=3), srt=90, col = "black")
text(2.5, 0.4,round(4.247821300948029, digits=3), srt=90, col = "black")

text(4.5, 0.4,round(1.8066831304229474, digits=3), srt=90, col = "black")
text(5.5, 0.4,round(2.3991582063920314, digits=3), srt=90, col = "black")

text(7.5, 0.4,round(0.6923256853908628, digits=3), srt=90, col = "black")
text(8.5, 0.4,round(2.3392476965292524, digits=3), srt=90, col = "black")

