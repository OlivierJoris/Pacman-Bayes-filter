confused <- c(3.3815262204238214, 3.2012568760391544)
afraid <- c(2.034467593791203, 2.521565219083069)
scared <- c(1.1547196316061477, 3.06720814248804)

colors <- c("blue", "green", "blue", "green", "blue", "green")

barplot(cbind(confused, afraid, scared), beside = TRUE, names.arg = c("confused", "afraid", "scared"), col = colors, ylim = c(0,4), main = "Mean entropy of Pacman belief state", ylab = "Mean entropy")
legend("topright", legend = c("large_filter layout", "large_filter_walls layout"), col=c("blue", "green"), pch = c(15,15))

text(1.5, 0.5,round(3.3815262204238214, digits=3), srt=90, col = "black")
text(2.5, 0.5,round(3.2012568760391544, digits=3), srt=90, col = "black")

text(4.5, 0.5,round(2.034467593791203, digits=3), srt=90, col = "black")
text(5.5, 0.5,round(2.521565219083069, digits=3), srt=90, col = "black")

text(7.5, 0.5,round(1.1547196316061477, digits=3), srt=90, col = "black")
text(8.5, 0.5,round(3.06720814248804, digits=3), srt=90, col = "black")

