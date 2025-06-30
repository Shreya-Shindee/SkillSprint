from typing import List, Optional
from pydantic import BaseModel, EmailStr
from datetime import datetime

# User Schemas
class UserBase(BaseModel):
    email: EmailStr
    username: str

class UserCreate(UserBase):
    password: str

class UserResponse(UserBase):
    id: int
    is_active: bool
    created_at: datetime
    total_xp: int = 0
    level: int = 1
    
    class Config:
        from_attributes = True

# Token Schemas
class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    username: Optional[str] = None

# Skill Schemas
class SkillBase(BaseModel):
    name: str
    description: Optional[str] = None
    parent_id: Optional[int] = None

class SkillCreate(SkillBase):
    pass

class SkillResponse(SkillBase):
    id: int
    
    class Config:
        from_attributes = True

class SkillTree(SkillResponse):
    children: List['SkillTree'] = []
    
    class Config:
        from_attributes = True

# Circular reference
SkillTree.update_forward_refs()

# Resource Schemas
class ResourceBase(BaseModel):
    title: str
    url: str
    description: Optional[str] = None
    resource_type: str
    skill_id: int

class ResourceCreate(ResourceBase):
    pass

class ResourceResponse(ResourceBase):
    id: int
    
    class Config:
        from_attributes = True

# Progress Schemas
class ProgressBase(BaseModel):
    skill_id: int
    progress_percentage: float
    completed: bool

class ProgressCreate(ProgressBase):
    pass

class ProgressUpdate(BaseModel):
    progress_percentage: Optional[float] = None
    completed: Optional[bool] = None

class ProgressResponse(ProgressBase):
    id: int
    user_id: int
    last_updated: datetime
    
    class Config:
        from_attributes = True

# XP Transaction Schemas
class XPTransactionBase(BaseModel):
    amount: int
    description: str

class XPTransactionCreate(XPTransactionBase):
    user_id: int

class XPTransactionResponse(XPTransactionBase):
    id: int
    user_id: int
    created_at: datetime
    
    class Config:
        from_attributes = True
        
# Skill decomposition and learning path schemas
class SkillNameRequest(BaseModel):
    skill_name: str
    
# Resource recommendation schema
class ResourceRecommendation(BaseModel):
    skill_name: str
    resources: List[ResourceResponse]

# Resource Interaction Schemas
class ResourceInteractionBase(BaseModel):
    resource_id: int
    skill_id: int

class ResourceInteractionCreate(ResourceInteractionBase):
    pass

class ResourceInteractionResponse(ResourceInteractionBase):
    id: int
    user_id: int
    clicked_at: datetime
    completed: bool
    completed_at: Optional[datetime] = None
    time_spent_minutes: Optional[int] = None
    
    class Config:
        from_attributes = True

# Resource Completion Schemas
class ResourceCompletionBase(BaseModel):
    resource_id: int
    skill_id: int

class ResourceCompletionCreate(ResourceCompletionBase):
    time_spent_minutes: Optional[int] = None

class ResourceCompletionResponse(ResourceCompletionBase):
    id: int
    user_id: int
    completed_at: datetime
    xp_awarded: int
    
    class Config:
        from_attributes = True

# Resource interaction tracking
class ResourceClickRequest(BaseModel):
    resource_id: int
    skill_id: int
    
class ResourceCompleteRequest(BaseModel):
    resource_id: int
    skill_id: int
    time_spent_minutes: Optional[int] = None
