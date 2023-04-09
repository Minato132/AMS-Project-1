library(ggplot2)
library(dplyr)
library(rlist)

data <- read.csv("Part B Data/binned_data")
data1 <- data[,c('x', 'y')]


# fit full model
full <- lm(y ~ poly(x, 2), data = data1)

# fit reduced model
reduced <- lm(y ~ x, data = data1)

print(anova(full, reduced))

plot <- ggplot(data1, aes(x=x, y=y)) + geom_point() + stat_smooth(method = 'lm', formula = y ~ x, size = 1) + xlab('x') + ylab('y') 
print(plot)