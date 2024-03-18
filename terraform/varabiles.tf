variable "security-group-name" {
  default = "store2-security-group"
  
}

variable "instance-type" {
  default = "t3.micro"
}

variable "key-name" {
  default = "store-server-key"
}

variable "env_prefix" {
  default = "dev"
  
}