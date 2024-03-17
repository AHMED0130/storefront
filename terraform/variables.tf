variable "security-group-name" {
  default = "store-security-group"
  
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