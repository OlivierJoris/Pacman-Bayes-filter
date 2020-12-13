confused <- c(4.571555420127652, 4.247821300948029)
afraid <- c(1.8066831304229474, 2.3991582063920314)
scared <- c(0.6923256853908628, 2.3392476965292524)

colors <- c("blue", "green", "blue", "green", "blue", "green")

barplot(cbind(confused, afraid, scared), beside = TRUE, names.arg = c("confused", "afraid", "scared"), col = colors, ylim = c(0,7), main = "Mean quality of Pacman's belief state", ylab = "Mean quality")
legend("topright", legend = c("large_filter layout", "large_filter_walls layout"), col=c("blue", "green"), pch = c(15,15))

arrows(x0=1.5, y0= 4.571555420127652 - 1.8975720253437058, x1=1.5, y1= 4.571555420127652 + 1.8975720253437058, code=3, angle=90, length=0.2, col="black", lwd=2)
text(1.5, 0.5,round(4.571555420127652, digits=3), srt=90, col = "black")

arrows(x0=2.5, y0= 4.247821300948029 - 1.960076197330298, x1=2.5, y1= 4.247821300948029 + 1.960076197330298, code=3, angle=90, length=0.2, col="black", lwd=2)
text(2.5, 0.5,round(4.247821300948029, digits=3), srt=90, col = "black")

arrows(x0=4.5, y0= 1.8066831304229474 - 0.9299983248054788, x1=4.5, y1= 1.8066831304229474 + 0.9299983248054788, code=3, angle=90, length=0.2, col="black", lwd=2)
text(4.5, 0.5,round(1.8066831304229474, digits=3), srt=90, col = "black")

arrows(x0=5.5, y0= 2.3991582063920314 - 1.2218522110573957, x1=5.5, y1= 2.3991582063920314 + 1.2218522110573957, code=3, angle=90, length=0.2, col="black", lwd=2)
text(5.5, 0.5,round(2.3991582063920314, digits=3), srt=90, col = "black")

arrows(x0=7.5, y0= 0.6923256853908628 - 0.4929771353961329, x1=7.5, y1= 0.6923256853908628 + 0.4929771353961329, code=3, angle=90, length=0.2, col="black", lwd=2)
text(7.15, 0.5,round(0.6923256853908628, digits=3), srt=90, col = "black")

arrows(x0=8.5, y0= 2.3392476965292524 - 1.9875154814545926, x1=8.5, y1= 2.3392476965292524 + 1.9875154814545926, code=3, angle=90, length=0.2, col="black", lwd=2)
text(8.15, 0.5,round(2.3392476965292524, digits=3), srt=90, col = "black")












