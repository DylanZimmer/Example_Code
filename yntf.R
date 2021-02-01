
library(dplyr)

yntf <- function(data) {

  A <- data
  
  #Lower all columns to make lowcols
  {
  lowcols <- as.data.frame(sapply(A, tolower))
  }

  #Makes the yntflist
  {
    counter <- 1
    yntflist <- matrix()
    yntfcheck <- matrix(c('yes','no','true','false','unknown',NA), ncol = 1)  
    uniqs <- apply(lowcols,2,unique)  #uniqs is a list
    uniqs <- lapply(uniqs,unlist)
    while(counter < length(uniqs)) {
      uvec <- as.vector(unlist(uniqs[counter]))
      if(all(uvec %in% yntfcheck) & length(uvec) > 2 & length(uvec) < 5) {
        yntflist <- c(yntflist,lowcols[counter])
      }
      counter <- counter + 1
    }
    yntflist <- lapply(yntflist,unlist)
    yntflist[1] <- NULL
  }
  
  #Make list1 & list2 to feed to makemats
  {
  list1 <- list()
  while(length(list1) < length(yntflist)^2) {
    list1 <- c(list1,yntflist)
  }
  
  list2 <- list()
  lcount <- 1
  counter <- 1
  while(length(list2) < length(yntflist)^2) {  
    while(lcount <= length(yntflist)) {
      list2 <- c(list2,yntflist[counter])
      lcount <- lcount + 1
    }
    lcount <- 1
    counter <- counter + 1
  }
  }
  
  #Makes the mats
  {
  matslist <- list()
  makematslist <- function(uugg,bbrr) {
    a1 = filter(A,uugg == 'yes' & bbrr == 'yes'
                | uugg == 'yes' & bbrr == 'true'
                | uugg == 'true' & bbrr == 'yes'
                | uugg == 'true' & bbrr == 'true') 
    a = count(a1)
    b1 = filter(A,uugg == 'yes' & bbrr == 'no'
                | uugg == 'yes' & bbrr == 'false'
                | uugg == 'true' & bbrr == 'no'
                | uugg == 'true' & bbrr == 'false')
    b = count(b1)
    c1 = filter(A,uugg == 'no' & bbrr == 'yes'
                | uugg == 'no' & bbrr == 'true'
                | uugg == 'false' & bbrr == 'yes'
                | uugg == 'false' & bbrr == 'true')
    c = count(c1)
    d1 = filter(A,uugg == 'no' & bbrr == 'no'
                | uugg == 'no' & bbrr == 'false'
                | uugg == 'false' & bbrr == 'no'
                | uugg == 'false' & bbrr == 'false')
    d = count(d1)
    matslist <- c(matslist,a,b,c,d)
    matslist <- return(matslist)
  }
  matslist <- mapply(makematslist,list1,bbrr = list2)
  mats <- as.matrix(matslist, nrow = 4)      #Why does it also give me 4, 5776 when I make nrow = 2?
  }
  
  #Gets your output
  {
    output2 <- data.frame()
    ctitles <- as.list(names(yntflist))
    rtitles <- list()
    titlecount <- 1
    counter <- 1
    while(length(rtitles) < 2*length(ctitles)) {
      while(titlecount <= 2) {
        rtitles <- c(rtitles,ctitles[counter])
        titlecount <- titlecount + 1
        }
      titlecount <- 1
      counter <- counter + 1
    }
    
    fish <- function(m) {
      bait <- unlist(m)
      fishin <- matrix(bait, nrow = 2)
      catchin <- fisher.test(fishin)
      output2 <- c(output2,catchin)
    }
    df <- data.frame()
    keep <- function(l) {
      df <- c(df,l[1],l[3])
      return(df)
    }
    
    output2 <- apply(mats,2,fish)
    output2 <- lapply(output2,keep)
    output2 <- unlist(output2)
    output <- as.matrix(output2)
    dim(output) <- c(2*length(yntflist),length(yntflist))
    colnames(output) <- ctitles
    rownames(output) <- rtitles
    write.csv(output, file = 'yntf.csv')
  }

}
